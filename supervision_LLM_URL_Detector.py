{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOpOyUZqdlg/iuibbSDZQpA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/King-tobe/Supervision-LLM-URL-phishing-detector/blob/main/supervision_LLM_URL_Detector.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Supervisioned Model Url Phishing Detector\n",
        "from urllib.parse import urlparse\n",
        "import pandas as pd\n",
        "\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.pipeline import Pipeline, FeatureUnion\n",
        "from sklearn.base import BaseEstimator, TransformerMixin\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.compose import ColumnTransformer\n",
        "\n",
        "\n",
        "urls = [\n",
        "    \"https://google.com\",\n",
        "    \"https://github.com\",\n",
        "    \"https://openai.com\",\n",
        "    \"https://microsoft.com\",\n",
        "    \"https://paytolltne.top/ezdrivema\",\n",
        "    \"https://uulh.bxynk.top/YnSk8W8l\",\n",
        "    \"http://login-paypal-security-alert.com\",\n",
        "    \"http://free-gift-card-password-reset.ru\",\n",
        "    \"http://verify-bank-account-now.com\",\n",
        "    \"http://appleid-login-confirm-security.com\"\n",
        "\n",
        "\n",
        "]\n",
        "\n",
        "labels = [\n",
        "    \"safe\",\n",
        "    \"safe\",\n",
        "    \"safe\",\n",
        "    \"safe\",\n",
        "    \"phishing\",\n",
        "    \"phishing\",\n",
        "    \"phishing\",\n",
        "    \"phishing\",\n",
        "    \"phishing\",\n",
        "    \"phishing\"\n",
        "]\n",
        "\n",
        "\n",
        "def extract_url_features(url):\n",
        "    parsed = urlparse(url)\n",
        "    domain = parsed.netloc\n",
        "\n",
        "    return {\n",
        "        \"url_length\": len(url),\n",
        "        \"domain_length\": len(domain),\n",
        "        \"num_dots\": url.count(\".\"),\n",
        "        \"num_hyphens\": url.count(\"-\"),\n",
        "        \"num_digits\": sum(char.isdigit() for char in url),\n",
        "        \"has_https\": int(parsed.scheme == \"https\"),\n",
        "        \"has_login\": int(\"login\" in url.lower()),\n",
        "        \"has_verify\": int(\"verify\" in url.lower()),\n",
        "        \"has_security\": int(\"security\" in url.lower()),\n",
        "        \"has_free\": int(\"free\" in url.lower()),\n",
        "        \"has_password\": int(\"password\" in url.lower()),\n",
        "    }\n",
        "\n",
        "\n",
        "feature_rows = [extract_url_features(url) for url in urls]\n",
        "df = pd.DataFrame(feature_rows)\n",
        "df[\"url\"] = urls\n",
        "\n",
        "model = Pipeline([\n",
        "    (\"features\", ColumnTransformer([\n",
        "        (\"text\", TfidfVectorizer(analyzer=\"char\", ngram_range=(3, 5)), \"url\"),\n",
        "        (\"manual\", StandardScaler(), [\n",
        "            \"url_length\",\n",
        "            \"domain_length\",\n",
        "            \"num_dots\",\n",
        "            \"num_hyphens\",\n",
        "            \"num_digits\",\n",
        "            \"has_https\",\n",
        "            \"has_login\",\n",
        "            \"has_verify\",\n",
        "            \"has_security\",\n",
        "            \"has_free\",\n",
        "            \"has_password\",\n",
        "        ])\n",
        "    ])),\n",
        "    (\"clf\", LogisticRegression())\n",
        "])\n",
        "\n",
        "model.fit(df, labels)\n",
        "\n",
        "test_url = \"https//google.com\"\n",
        "\n",
        "test_df = pd.DataFrame([extract_url_features(test_url)])\n",
        "test_df[\"url\"] = [test_url]\n",
        "\n",
        "print(model.predict(test_df))\n",
        "print(model.predict_proba(test_df))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ba1aac8-379c-4c77-dfe1-d1e1ce0ae9a8",
        "cellView": "form",
        "id": "sU7W0jSy9Krb"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['safe']\n",
            "[[0.14865385 0.85134615]]\n"
          ]
        }
      ]
    }
  ]
}