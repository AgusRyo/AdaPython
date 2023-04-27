{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNDyvUP5ZZ8qUPRk/AFwMVn",
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
        "<a href=\"https://colab.research.google.com/github/AgusRyo/AdaPython/blob/main/Proyecto_Final.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E2eHCLJzuwqT",
        "outputId": "f067b641-34a0-4707-d022-e81b627a1e0a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting flask_ngrok\n",
            "  Downloading flask_ngrok-0.0.25-py3-none-any.whl (3.1 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from flask_ngrok) (2.27.1)\n",
            "Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.9/dist-packages (from flask_ngrok) (2.2.3)\n",
            "Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask_ngrok) (2.2.3)\n",
            "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask_ngrok) (8.1.3)\n",
            "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask_ngrok) (2.1.2)\n",
            "Requirement already satisfied: importlib-metadata>=3.6.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask_ngrok) (6.6.0)\n",
            "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask_ngrok) (3.1.2)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.9/dist-packages (from requests->flask_ngrok) (2.0.12)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests->flask_ngrok) (1.26.15)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->flask_ngrok) (3.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests->flask_ngrok) (2022.12.7)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/dist-packages (from importlib-metadata>=3.6.0->Flask>=0.8->flask_ngrok) (3.15.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.9/dist-packages (from Jinja2>=3.0->Flask>=0.8->flask_ngrok) (2.1.2)\n",
            "Installing collected packages: flask_ngrok\n",
            "Successfully installed flask_ngrok-0.0.25\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyngrok==4.1.1\n",
            "  Downloading pyngrok-4.1.1.tar.gz (18 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.9/dist-packages (from pyngrok==4.1.1) (0.18.3)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.9/dist-packages (from pyngrok==4.1.1) (6.0)\n",
            "Building wheels for collected packages: pyngrok\n",
            "  Building wheel for pyngrok (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyngrok: filename=pyngrok-4.1.1-py3-none-any.whl size=15979 sha256=02479cfe8af92e1404f77691baeee4e91a84575f7ea25235ac6b8305302b1e0f\n",
            "  Stored in directory: /root/.cache/pip/wheels/89/2d/c2/abe6bcfde6bce368c00ecd73310c11edb672c3eda09a090cfa\n",
            "Successfully built pyngrok\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-4.1.1\n",
            "Authtoken saved to configuration file: /root/.ngrok2/ngrok.yml\n"
          ]
        }
      ],
      "source": [
        "!pip install flask_ngrok\n",
        "!pip install pyngrok==4.1.1   \n",
        "!ngrok authtoken 2OhokiiPdAj2opRcxbHsZPLcQol_6vPCHNpUHuDqueFoA78oF"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from flask import Flask\n",
        "from flask_ngrok import run_with_ngrok\n",
        "\n",
        "app=Flask(__name__)\n",
        "run_with_ngrok(app)\n",
        "\n",
        "@app.route(\"/\")\n",
        "def home():\n",
        "  return \"<h1>Probando....</h1>\"\n",
        "\n",
        "app.run() \n"
      ],
      "metadata": {
        "id": "wGMGNN0BvdIz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/gdrive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A6S2JwgyxM2B",
        "outputId": "df79032e-9a55-43eb-e09e-1e1bce8c8ec1"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/gdrive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from flask.templating import render_template\n",
        "from flask import Flask\n",
        "from flask_ngrok import run_with_ngrok\n",
        "template_folder= '/content/gdrive/MyDrive/Colab Notebooks/Proyecto_ADA/template'\n",
        "app= Flask(__name__, template_folder = template_folder)\n",
        "run_with_ngrok(app)\n",
        "@app.route(\"/\")\n",
        "@app.route(\"/home\")\n",
        "def home():\n",
        "  return render_template('home.html')\n",
        "\n",
        "app.run()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4eysJp1lvpkB",
        "outputId": "03d601de-021d-46cd-8b39-0331860dbfcf"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " * Serving Flask app '__main__'\n",
            " * Debug mode: off\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
            " * Running on http://127.0.0.1:5000\n",
            "INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " * Running on http://6d12-35-197-82-194.ngrok-free.app\n",
            " * Traffic stats available on http://127.0.0.1:4040\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug:127.0.0.1 - - [27/Apr/2023 13:06:44] \"GET / HTTP/1.1\" 200 -\n",
            "INFO:werkzeug:127.0.0.1 - - [27/Apr/2023 13:06:45] \"\u001b[33mGET /style.css HTTP/1.1\u001b[0m\" 404 -\n",
            "INFO:werkzeug:127.0.0.1 - - [27/Apr/2023 13:06:46] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"
          ]
        }
      ]
    }
  ]
}