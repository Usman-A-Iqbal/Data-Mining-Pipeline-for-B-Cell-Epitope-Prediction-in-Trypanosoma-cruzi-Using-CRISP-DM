{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WzMo-tDdHj-j"
      },
      "source": [
        "#**Data Mining Coursework**\n",
        "\n",
        "Student: Usman Iqbal\n",
        "\n",
        "The course work follows the CRISP-DM pipeline, which is an iterative methodology. The stages are as follow Explanatory Data Analysis, Data preprossesing, Modelling, Testing, Hyperparameter tuning, Evalutation.\n",
        "\n",
        "The programming language used is Python as well as Python Data Science libraries including Numpy, Pandas, Matplotlib and SciKit Learn.\n",
        "\n",
        "This Coursework was developed using Google Colab.\n",
        "\n",
        "Every attempt was made to make the process as reproducable as possible."
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Explanatory Data Analysis**"
      ],
      "metadata": {
        "id": "WE-958D9XI9M"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Importing packages"
      ],
      "metadata": {
        "id": "qqxHYVZwA8p2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "from sklearn.model_selection import GroupShuffleSplit\n",
        "from sklearn.ensemble import IsolationForest\n",
        "from sklearn.preprocessing import MinMaxScaler\n",
        "from sklearn.metrics import balanced_accuracy_score, classification_report\n",
        "from sklearn.feature_selection import SelectKBest, mutual_info_classif\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\n"
      ],
      "metadata": {
        "id": "_GDwMVDGA7wt"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1) Importing the file into the notebook as a dataframe"
      ],
      "metadata": {
        "id": "qazGrDlxwfg7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "path = \"df_reduced.csv\"\n",
        "df = pd.read_csv(path ,sep=';')\n",
        "\n",
        "# shows the rows (observations), columns (varibales) and provides the total of the diffetent types of variable types\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Nh6DFXDv7V-",
        "outputId": "5b31d8ef-e32e-4409-9fa4-6e7f28a629b2"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 12402 entries, 0 to 12401\n",
            "Columns: 300 entries, Info_PepID to feat_esm1b_289\n",
            "dtypes: float64(290), int64(4), object(6)\n",
            "memory usage: 28.4+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2) Checking the missing values in the columns and the total number of missing values"
      ],
      "metadata": {
        "id": "Nm_TVKETwv1F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(end = \"\\n \\n \\n\")\n",
        "# shows the missing data across the columns\n",
        "missing_values = df.isnull()\n",
        "print(missing_values.sum())\n",
        "\n",
        "print(end = \"\\n \\n \\n\")\n",
        "\n",
        "# shows the total number of missing values in the entire dataset\n",
        "df.isnull().sum().sum()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s0oSxL0Kv_eX",
        "outputId": "707f3a5d-c632-465b-83cf-dcf84f3dee67"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            " \n",
            " \n",
            "Info_PepID           0\n",
            "Info_organism_id     0\n",
            "Info_protein_id      0\n",
            "Info_pos             0\n",
            "Info_AA              0\n",
            "                    ..\n",
            "feat_esm1b_285      13\n",
            "feat_esm1b_286      14\n",
            "feat_esm1b_287      11\n",
            "feat_esm1b_288      13\n",
            "feat_esm1b_289      14\n",
            "Length: 300, dtype: int64\n",
            "\n",
            " \n",
            " \n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "14993"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3) Removing the Info variables (as they have no predictive value) and printing out a feature summary of the reamining values"
      ],
      "metadata": {
        "id": "geR1_Ew7w_vI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Identify and separate the feature variables\n",
        "info_variables = ['Info_PepID','Info_organism_id', 'Info_protein_id', 'Info_pos', 'Info_AA', 'Info_epitope_id', 'Info_nPos', 'Info_nNeg']  # Add the names of informational variables\n",
        "df = df.drop(info_variables, axis=1)\n",
        "feature_variables = df\n",
        "\n",
        "# Perform exploratory analysis on feature variables\n",
        "# For example, you can use describe() to get summary statistics\n",
        "feature_summary = feature_variables.describe()\n",
        "\n",
        "# Display the summary statistics\n",
        "print(\"Summary statistics for feature variables:\")\n",
        "print(feature_summary)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FsW71mlIwI2j",
        "outputId": "79f5082e-982a-4d38-c5a0-8e022da8d54f"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Summary statistics for feature variables:\n",
            "       Info_cluster         Class  feat_esm1b_0  feat_esm1b_1  feat_esm1b_2  \\\n",
            "count  12402.000000  12402.000000  12388.000000  12388.000000  12390.000000   \n",
            "mean     139.667634     -0.970005      0.040924      0.150334      0.068379   \n",
            "std       77.944928      0.243095      0.194674      0.180886      0.206083   \n",
            "min        7.000000     -1.000000     -0.739531     -0.664717     -0.918128   \n",
            "25%       70.000000     -1.000000     -0.084004      0.040529     -0.065351   \n",
            "50%      145.000000     -1.000000      0.034410      0.145975      0.069221   \n",
            "75%      205.000000     -1.000000      0.160128      0.255262      0.203641   \n",
            "max      283.000000      1.000000      0.925082      1.203393      0.974194   \n",
            "\n",
            "       feat_esm1b_3  feat_esm1b_4  feat_esm1b_5  feat_esm1b_6  feat_esm1b_7  \\\n",
            "count  12389.000000  12390.000000  12388.000000  12388.000000  12390.000000   \n",
            "mean       0.077347      0.023808     -0.136817     -0.094994     -0.008023   \n",
            "std        0.183967      0.193493      0.193170      0.219265      0.240700   \n",
            "min       -0.931084     -1.010501     -1.086608     -1.499195     -0.957883   \n",
            "25%       -0.039926     -0.097352     -0.260591     -0.207169     -0.180765   \n",
            "50%        0.081350      0.035148     -0.135299     -0.071583     -0.034287   \n",
            "75%        0.201316      0.155194     -0.012340      0.051047      0.152728   \n",
            "max        1.217404      0.709081      0.838205      0.582508      1.275659   \n",
            "\n",
            "       ...  feat_esm1b_280  feat_esm1b_281  feat_esm1b_282  feat_esm1b_283  \\\n",
            "count  ...    12388.000000    12388.000000    12388.000000    12389.000000   \n",
            "mean   ...        0.097165        0.071550       -0.053270       -0.085493   \n",
            "std    ...        0.220632        0.192462        0.195300        0.273192   \n",
            "min    ...       -1.035132       -0.987730       -0.898706       -1.284584   \n",
            "25%    ...       -0.042771       -0.047586       -0.178838       -0.278291   \n",
            "50%    ...        0.097722        0.078830       -0.059335       -0.087916   \n",
            "75%    ...        0.243582        0.199581        0.066225        0.101746   \n",
            "max    ...        1.003307        0.966091        0.964062        1.041853   \n",
            "\n",
            "       feat_esm1b_284  feat_esm1b_285  feat_esm1b_286  feat_esm1b_287  \\\n",
            "count    12388.000000    12389.000000    12388.000000    12391.000000   \n",
            "mean         0.031548        0.064117       -0.073711       -0.138898   \n",
            "std          0.232971        0.205014        0.189592        0.203090   \n",
            "min         -1.076593       -1.045234       -1.043452       -0.982278   \n",
            "25%         -0.106314       -0.065745       -0.191607       -0.271883   \n",
            "50%          0.048964        0.058741       -0.080203       -0.137899   \n",
            "75%          0.193762        0.192159        0.037429       -0.007596   \n",
            "max          0.842581        1.056373        0.898551        0.708880   \n",
            "\n",
            "       feat_esm1b_288  feat_esm1b_289  \n",
            "count    12389.000000    12388.000000  \n",
            "mean        -0.055978        0.116088  \n",
            "std          0.191709        0.210566  \n",
            "min         -0.860550       -1.059898  \n",
            "25%         -0.187564        0.008592  \n",
            "50%         -0.061822        0.132910  \n",
            "75%          0.066036        0.246717  \n",
            "max          0.921726        0.992171  \n",
            "\n",
            "[8 rows x 292 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4) Visualising the missing values per column and per row"
      ],
      "metadata": {
        "id": "hsC3POr0xaLN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#####Plots the counts of the missing values per column######\n",
        "# Check for missing values\n",
        "missing_values = df.isnull().sum()\n",
        "\n",
        "# Plot the count of missing values per column on a scatter plot\n",
        "plt.figure(figsize=(10, 6)) # the number of inches\n",
        "plt.scatter(missing_values.index, missing_values.values, color='blue')\n",
        "plt.title('Count of Missing Values per Column')\n",
        "plt.xlabel('Columns')\n",
        "plt.ylabel('Count of Missing Values')\n",
        "#plt.xticks(rotation=90)  # Rotate x-axis labels for better readability\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n",
        "\n",
        "# Check for missing values per row\n",
        "missing_values_per_row = df.isnull().sum(axis=1)\n",
        "\n",
        "# Plot the count of missing values per row on a scatter plot\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.scatter(df.index, missing_values_per_row, color='red')\n",
        "plt.title('Count of Missing Values per Row')\n",
        "plt.xlabel('Rows')\n",
        "plt.ylabel('Count of Missing Values')\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "bzxx5kZRwWxh",
        "outputId": "87f47c7e-15d5-4a67-bb89-ad77b8b1a514"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3oAAAIjCAYAAABVpWnzAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABfyUlEQVR4nO3de3zP9f//8ft723snzIjZ5rgcck6pWMqhMKKI+GBFcuhAH4c+lD7lVOlHB4SSDuiTlVLJBw3RCUM5RKQop8IktrHZ+fn7Y9+9P95t0/tt79nby+16ubwve7+fr+fr+by/3ntP70evk80YYwQAAAAAsAyf0g4AAAAAAPAsCj0AAAAAsBgKPQAAAACwGAo9AAAAALAYCj0AAAAAsBgKPQAAAACwGAo9AAAAALAYCj0AAAAAsBgKPQAAAACwGAo9AICys7M1duxYVa9eXT4+PurevbvH51iwYIFsNpsOHjzo0XG//PJL2Ww2ffnllx4dtzQcPHhQNptNCxYsKO0oVxQrfYYAIB+FHgD8n19++UUPPvigrr76agUGBiokJEStWrXSzJkzde7cudKOJ0l69dVXS6QIePvtt/XCCy/onnvu0cKFCzVq1Kgi+7Zt21Y2m01169YtdPmaNWtks9lks9m0ZMkSj2f1FnfddZeCg4N15syZIvvExsbK399ff/755yVMZn05OTmaP3++2rZtq4oVKyogIEC1atXSwIED9d1335V2PADwCn6lHQAAvMGKFSvUq1cvBQQEqH///mrcuLEyMzO1fv16jRkzRrt379a8efNKO6ZeffVVVapUSffff79Hx123bp2qVq2q6dOnu9Q/MDBQ+/fv15YtW3TTTTc5LVu0aJECAwOVnp7u1H7fffepT58+CggI8FhuSWrdurXOnTsnf39/j477d2JjY/Xf//5Xn3zyifr3719geVpamj799FN16tRJV1111SXNZmXnzp1Tjx49FB8fr9atW+vJJ59UxYoVdfDgQX3wwQdauHChDh8+rGrVqpV2VAAoVRR6AK54Bw4cUJ8+fVSzZk2tW7dOERERjmXDhg3T/v37tWLFilJMWPJOnDih0NBQl/vXrl1b2dnZeu+995wKvfT0dH3yySfq0qWLPvroI6d1fH195evr66nIDj4+PgoMDPT4uH/nrrvuUrly5RQXF1dooffpp58qNTVVsbGxlzzb5Sw7O1u5ublFFu5jxoxRfHy8pk+frpEjRzotmzBhgsv/swIArI5DNwFc8aZNm6azZ8/qrbfeciry8tWpU0cjRoxwvM7OztYzzzyj2rVrOw4Ze/LJJ5WRkeG0ns1m08SJEwuMV6tWLac9cvnnrm3YsEGjR49W5cqVVaZMGd199936448/nNbbvXu3vvrqK8ehkW3btr3gtqWmpuqxxx5T9erVFRAQoGuuuUYvvviijDGS/ndO2BdffKHdu3c7xnXlXKW+fftq8eLFys3NdbT997//VVpamnr37l2gf2Hn6H333XeKiYlRpUqVFBQUpKioKD3wwANO673//vtq3ry5ypUrp5CQEDVp0kQzZ850LC/s/Kq2bduqcePG2rNnj9q1a6fg4GBVrVpV06ZNK5Dr0KFDuuuuu1SmTBmFhYVp1KhRWrVq1d++D0FBQerRo4fWrl2rEydOFFgeFxencuXK6a677tKpU6f0r3/9S02aNFHZsmUVEhKizp076/vvvy9y/PO3pbDf8/33369atWo5teXm5mrGjBlq1KiRAgMDVaVKFT344IM6ffq0Uz9X3vfC1KpVS127dtXq1avVrFkzBQYGqmHDhvr4448L9E1KStLIkSMdn706depo6tSpTp+X/M/fiy++qBkzZjj+pvbs2VPo/L/99ptef/11dejQoUCRJ+X9z4R//etfTnvztm/frs6dOyskJERly5bV7bffrk2bNrm0rYXtOf/r7yP/8/fBBx9o0qRJqlq1qsqVK6d77rlHycnJysjI0MiRIxUWFqayZctq4MCBhf5bMXz4cC1dulSNGzdWQECAGjVqpPj4+L/NCQBFYY8egCvef//7X1199dW6+eabXeo/ePBgLVy4UPfcc48ee+wxbd68Wc8//7x+/PFHffLJJxed49FHH1WFChU0YcIEHTx4UDNmzNDw4cO1ePFiSdKMGTP06KOPqmzZsvr3v/8tSapSpUqR4xljdNddd+mLL77QoEGD1KxZM61atUpjxozR77//runTp6ty5cr6z3/+o+eee05nz57V888/L0lq0KDB3+bt16+fJk6cqC+//FK33XabpLzi5vbbb1dYWNjfrn/ixAl17NhRlStX1hNPPKHQ0FAdPHjQqWhYs2aN+vbtq9tvv11Tp06VJP3444/asGGDU/FdmNOnT6tTp07q0aOHevfurSVLlujxxx9XkyZN1LlzZ0l5hfBtt92mY8eOacSIEQoPD1dcXJy++OKLv80v5R2+uXDhQn3wwQcaPny4o/3UqVNatWqV+vbtq6CgIO3evVtLly5Vr169FBUVpcTERL3++utq06aN9uzZo8jISJfm+zsPPvigFixYoIEDB+qf//ynDhw4oNmzZ2v79u3asGGD7Ha7S+/7hezbt0//+Mc/9NBDD2nAgAGaP3++evXqpfj4eHXo0EFS3mGrbdq00e+//64HH3xQNWrU0MaNGzVu3DgdO3ZMM2bMcBpz/vz5Sk9P19ChQxUQEKCKFSsWOvdnn32m7Oxs3XfffS5l3b17t2699VaFhIRo7Nixstvtev3119W2bVt99dVXatGihUvjuOL5559XUFCQnnjiCe3fv1+zZs2S3W6Xj4+PTp8+rYkTJ2rTpk1asGCBoqKiNH78eKf1169fr48//liPPPKIypUrp1deeUU9e/bU4cOHOfQXwMUxAHAFS05ONpJMt27dXOq/Y8cOI8kMHjzYqf1f//qXkWTWrVvnaJNkJkyYUGCMmjVrmgEDBjhez58/30gy7du3N7m5uY72UaNGGV9fX5OUlORoa9SokWnTpo1LWZcuXWokmWeffdap/Z577jE2m83s37/f0damTRvTqFEjl8Y9v+8NN9xgBg0aZIwx5vTp08bf398sXLjQfPHFF0aS+fDDDwts54EDB4wxxnzyySdGkvn222+LnGvEiBEmJCTEZGdnF9knf64vvvjCKaMk88477zjaMjIyTHh4uOnZs6ej7aWXXjKSzNKlSx1t586dM/Xr1y8wZmGys7NNRESEiY6OdmqfO3eukWRWrVpljDEmPT3d5OTkOPU5cOCACQgIMJMnT3Zqk2Tmz5/vtC2F/c4HDBhgatas6Xj9zTffGElm0aJFTv3i4+Od2l1534tSs2ZNI8l89NFHjrbk5GQTERFhrrvuOkfbM888Y8qUKWN+/vlnp/WfeOIJ4+vraw4fPuy0vSEhIebEiRN/O/+oUaOMJLN9+3aX8nbv3t34+/ubX375xdF29OhRU65cOdO6dWtHW2Gfob/+neb76+8jf93GjRubzMxMR3vfvn2NzWYznTt3dlo/Ojra6fdmTN6/Ff7+/k5/k99//72RZGbNmuXStgLAX3HoJoArWkpKiiSpXLlyLvVfuXKlJGn06NFO7Y899pgkFetcvqFDh8pmszle33rrrcrJydGhQ4cuaryVK1fK19dX//znPwtkNcbos88+u+is+fr166ePP/5YmZmZWrJkiXx9fXX33Xe7tG7+OYHLly9XVlZWkX1SU1O1Zs0at7OVLVtW9957r+O1v7+/brrpJv3666+Otvj4eFWtWlV33XWXoy0wMFBDhgxxaQ5fX1/16dNHCQkJToekxsXFqUqVKrr99tslSQEBAfLxyftPbk5Ojv7880+VLVtW11xzjbZt2+b2thXmww8/VPny5dWhQwedPHnS8WjevLnKli3r2Evpyvt+IZGRkU6/45CQEPXv31/bt2/X8ePHHVluvfVWVahQwSlL+/btlZOTo6+//tppzJ49e6py5cp/O7c7f685OTlavXq1unfvrquvvtrRHhERoX79+mn9+vWO8Tyhf//+stvtjtctWrSQMabAIbEtWrTQkSNHlJ2d7dTevn171a5d2/G6adOmCgkJcfq8AoA7KPQAXNFCQkIk6YKXyD/foUOH5OPjozp16ji1h4eHKzQ09KKLMkmqUaOG0+sKFSpIUoHzq1x16NAhRUZGFvhSnH9YZnGy5uvTp4+Sk5P12WefadGiReratavLRXObNm3Us2dPTZo0SZUqVVK3bt00f/58p/OXHnnkEdWrV0+dO3dWtWrV9MADD7h83lK1atWcCmcp7z09//08dOiQateuXaDfX3+/F5J/sZW4uDhJeeeRffPNN+rTp4/j4jO5ubmaPn266tatq4CAAFWqVEmVK1fWzp07lZyc7PJcF7Jv3z4lJycrLCxMlStXdnqcPXvWcR6hK+/7hdSpU6fA+1WvXj1JchS7+/btU3x8fIEc7du3l6QC5zRGRUW5NLc7f69//PGH0tLSdM011xRY1qBBA+Xm5urIkSMuzeuKv/79li9fXpJUvXr1Au25ubkFfu9/XV8q+HkFAHdwjh6AK1pISIgiIyP1ww8/uLXeX7/ouiMnJ6fQ9qKuSGn+78Ip3igiIkJt27bVSy+9pA0bNhS40uaF5N9nb9OmTfrvf/+rVatW6YEHHtBLL72kTZs2qWzZsgoLC9OOHTu0atUqffbZZ/rss880f/589e/fXwsXLrzg+Jfq/WzevLnq16+v9957T08++aTee+89GWOcrrY5ZcoUPf3003rggQf0zDPPqGLFivLx8dHIkSOdLk5SGJvNVmjmv36OcnNzFRYWpkWLFhU6Tv4eM1fe9+LKzc1Vhw4dNHbs2EKX5xeG+YKCglwat379+pKkXbt2qVmzZsXK+HeK+hvPyckp9LNV1OfN1c/h5fj3D8C7UegBuOJ17dpV8+bNU0JCgqKjoy/Yt2bNmsrNzdW+ffucLliSmJiopKQk1axZ09FWoUIFJSUlOa2fmZmpY8eOXXRWdwrMmjVr6vPPP9eZM2ec9rLt3bvXsdwT+vXrp8GDBys0NFR33HGH2+u3bNlSLVu21HPPPae4uDjFxsbq/fff1+DBgyXlHXJ555136s4771Rubq4eeeQRvf7663r66afd2vNWmJo1a2rPnj0yxji9t/v373drnNjYWD399NPauXOn4uLiVLduXd14442O5UuWLFG7du301ltvOa2XlJSkSpUqXXDsChUqFHr43l/3yNauXVuff/65WrVq5VLh9Hfve1H2799f4P36+eefJclxFdDatWvr7Nmzjj14ntK5c2f5+vrq3Xff/dsLslSuXFnBwcH66aefCizbu3evfHx8CuxtO19hf79S3vt+/qGgAOCtOHQTwBVv7NixKlOmjAYPHqzExMQCy3/55RfH5fzzC5m/XjXw5ZdfliR16dLF0Va7du0C5yLNmzevyD16rihTpkyhXz4Lc8cddygnJ0ezZ892ap8+fbpsNpvjypPFdc8992jChAl69dVX3bpp+enTpwvsrcjfS5N/GOGff/7ptNzHx0dNmzZ16lMcMTEx+v3337Vs2TJHW3p6ut544w23xsnfezd+/Hjt2LGjwL3zfH19C2zrhx9+qN9///1vx65du7b27t3rdKuN77//Xhs2bHDq17t3b+Xk5OiZZ54pMEZ2drbjc+PK+34hR48edbq6bEpKit555x01a9ZM4eHhjiwJCQlatWpVgfWTkpIKnJ/mqurVq2vIkCFavXq1Zs2aVWB5bm6uXnrpJf3222/y9fVVx44d9emnnzqdP5mYmKi4uDjdcsstjkNBC1O7dm1t2rRJmZmZjrbly5d79HBPAChJ7NEDcMWrXbu24uLi9I9//EMNGjRQ//791bhxY2VmZmrjxo368MMPHffTuvbaazVgwADNmzdPSUlJatOmjbZs2aKFCxeqe/fuateunWPcwYMH66GHHlLPnj3VoUMHff/991q1atXf7sG5kObNm+u1117Ts88+qzp16igsLMxxa4O/uvPOO9WuXTv9+9//1sGDB3Xttddq9erV+vTTTzVy5EinCz8UR/ny5Qu9X+DfWbhwoV599VXdfffdql27ts6cOaM33nhDISEhjoJ68ODBOnXqlG677TZVq1ZNhw4d0qxZs9SsWTOXbgHxdx588EHNnj1bffv21YgRIxQREaFFixY5bsDu6h7UqKgo3Xzzzfr0008lqUCh17VrV02ePFkDBw7UzTffrF27dmnRokUu7Rl64IEH9PLLLysmJkaDBg3SiRMnNHfuXDVq1MjpYiJt2rTRgw8+qOeff147duxQx44dZbfbtW/fPn344YeaOXOm7rnnHpfe9wupV6+eBg0apG+//VZVqlTR22+/rcTERM2fP9/RZ8yYMVq2bJm6du2q+++/X82bN1dqaqp27dqlJUuW6ODBgxf9d/DSSy/pl19+0T//+U99/PHH6tq1qypUqKDDhw/rww8/1N69e9WnTx9J0rPPPqs1a9bolltu0SOPPCI/Pz+9/vrrysjIKPSeiucbPHiwlixZok6dOql379765Zdf9O6773rs7wYASlypXOsTALzQzz//bIYMGWJq1apl/P39Tbly5UyrVq3MrFmzTHp6uqNfVlaWmTRpkomKijJ2u91Ur17djBs3zqmPMcbk5OSYxx9/3FSqVMkEBwebmJgYs3///iJvr/DXy90Xdsn348ePmy5duphy5coZSX97q4UzZ86YUaNGmcjISGO3203dunXNCy+84HQbB2Mu/vYKRXHl9grbtm0zffv2NTVq1DABAQEmLCzMdO3a1Xz33XeOdZYsWWI6duxowsLCjL+/v6lRo4Z58MEHzbFjxwrM9dfbKxSW8a+3JDDGmF9//dV06dLFBAUFmcqVK5vHHnvMfPTRR0aS2bRpk0vviTHGzJkzx0gyN910U4Fl6enp5rHHHjMREREmKCjItGrVyiQkJBS4VH9ht1cwxph3333XXH311cbf3980a9bMrFq1qtBtMcaYefPmmebNm5ugoCBTrlw506RJEzN27Fhz9OhRY4xr73tRatasabp06WJWrVplmjZtagICAkz9+vWdfs/5zpw5Y8aNG2fq1Klj/P39TaVKlczNN99sXnzxRcdtCPK394UXXvjbuc+XnZ1t3nzzTXPrrbea8uXLG7vdbmrWrGkGDhxY4NYL27ZtMzExMaZs2bImODjYtGvXzmzc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QkIK3ZsnSQEBAQoICCjQbrfbC9xyorScn8PPz6/Itgst8+YxyE1ub52T3OQmt/fNSe7LL/eVvO3kLt4Y3vB9vLTnlzx4MZaEhAQFBgZ6ajhJ0u23365du3Zpx44djscNN9yg2NhYx3O73a61a9c61vnpp590+PBhRUdHS5Kio6O1a9cunThxwtFnzZo1CgkJUcOGDR19zh8jv0/+GAAAAABwOfFzd4UePXo4vTbG6NixY/ruu+/09NNPeyyYJJUrV06NGzd2aitTpoyuuuoqR/ugQYM0evRoVaxYUSEhIXr00UcVHR2tli1bSpI6duyohg0b6r777tO0adN0/PhxPfXUUxo2bJhjj9xDDz2k2bNna+zYsXrggQe0bt06ffDBB1qxYoVHtwcAAAAALgW3C73y5cs7vfbx8dE111yjyZMnq2PHjh4L5qrp06fLx8dHPXv2VEZGhmJiYvTqq686lvv6+mr58uV6+OGHFR0drTJlymjAgAGaPHmyo09UVJRWrFihUaNGaebMmapWrZrefPNN7qEHAAAA4LLkdqE3f/78ksjhsi+//NLpdWBgoObMmaM5c+YUuU7NmjW1cuXKC47btm1bbd++3RMRAQAAAKBUuV3o5du6dat+/PFHSVKjRo103XXXeSwUAAAAAODiuV3onThxQn369NGXX37puNJlUlKS2rVrp/fff1+VK1f2dEYAAAAAgBvcvurmo48+qjNnzmj37t06deqUTp06pR9++EEpKSn65z//WRIZAQAAAABucHuPXnx8vD7//HM1aNDA0dawYUPNmTOnVC7GAgAAAABw5vYevdzc3EJvAGi325Wbm+uRUAAAAACAi+d2oXfbbbdpxIgROnr0qKPt999/16hRo3T77bd7NBwAAAAAwH1uF3qzZ89WSkqKatWqpdq1a6t27dqKiopSSkqKZs2aVRIZAQAAAABucPscverVq2vbtm36/PPPtXfvXklSgwYN1L59e4+HAwAAAAC476Luo2ez2dShQwd16NDB03kAAAAAAMXk8qGb69atU8OGDZWSklJgWXJysho1aqRvvvnGo+EAAAAAAO5zudCbMWOGhgwZopCQkALLypcvrwcffFAvv/yyR8MBAAAAANzncqH3/fffq1OnTkUu79ixo7Zu3eqRUAAAAACAi+dyoZeYmFjo/fPy+fn56Y8//vBIKAAAAADA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chIpKytLaWlpjiz5zy/U5m5/bxmD3OT21jnJTW5ye9+c5L78cl/J207u4o1ht9tVmvJz5dcIpYFCz0POnDkjSapevXopJwEAAADgDc6cOaPy5cuXytwcuukhkZGROnLkiJKSkpScnFyqjyNHjkiSjhw54ni+Z8+eItsutMybxyA3ub11TnKTm9zeNye5L7/cV/K2k7t4Yxw5cqTUv48nJSXpyJEjioyMVGlhj56H+Pj4qFq1aqUdw0lISIjjebly5Ypsu9Aybx6D3OT21jnJTW5ye9+c5L78cl/J207u4o0REhLi1F5aSmtPXj726AEAAACAxVDoAQAAAIDFcOimBQUEBGjChAkKCAiQJE2YMEEhISFFtl1omTePQW5ye+uc5CY3ub1vTnJffrmv5G0nd/HGyG+70tlMaV7zEwAAAADgcRy6CQAAAAAWQ6EHAAAAABZDoQcAAAAAVmPgltzcXDNkyBATGhpqJJmQkBAjyfTo0eOCbeXKlXP66evrayQZScZutzue5z9uu+22AuteaK6WLVsW2b9p06YXndfV/vltkkyZMmWMJBMcHFxgu/LHPf+R3z//51+fn/+IiYkptL2wcQtru5j+npjTnTGK6u8tY3jTnEWNUa1atULbC/uMufs59cTnujTGKKy/VT4fl2vuovpfrrm95XfsTf/2u9O/JHN7++e1JD9/pfFeleQYJTXnihUrjCSzfft2c+DAgYtqK40xSmrO7du3l3bJ4REUem5auXKlsdvt5sUXXzR2u93ExMSY66+/3qntq6++Mu+++65T29SpU43dbjd9+/Y1VatWNX5+fmbixInG19fX2Gw2U7VqVSPlFWVz5swxPj4+plGjRsbHx8fUrVvX+Pj4mMDAQMcfZNmyZY3NZjOtWrUykozNZnP0DwkJMTabzURGRhopr6i84YYbjM1mc+TNH//8bTi/7frrry/QPywsrNB/LGw2W5H/GHmiPw8ePHjw4MGDBw8el/vDne/Afn5+pnz58iYgIMA0bdrUfPbZZ27XLRy66aZffvlFERERCggIUEREhMLDw5WVleXU1rp1a50+fdqpLTg4WBEREcrMzFTVqlUVGRmpq666SiEhIQoODlZubq5sNpuioqKUm5uroKAg+fj4KDAwUAcOHJCvr69atmypevXqKSgoSGXLlpUkVapUSZLk7+8vHx8fp/WCgoJks9kUEhLiaMvPm9/v/G04v83Pz69Af/N/F2gNCwuTJNntdklSSEiIqlWrVuC9ys/oavtVV13leO7jU/hHs6j2othsthLpi0vPz6/g3WDc/TwU1t/dMdxV0uO7yltywBn/7pQ+fgfAxbHy38752xYUFCRJ8vX1dXscf39/p/HMeTc78Pf3V7ly5XTttdeqRo0aatCggex2u0aMGCFJCgwMlI+Pj/r166eHHnpId999t7Zv3+7edhjD7RVcdf/992vhwoWlHQMAAADAJeDn56fs7GyFhoYqJCREhw8fdizz9/eXzWZTZmamfHx8lJOTI5vNJn9/f2VkZKhbt25atmyZJKlMmTI6e/aso+iLiIhQYmKizp07p7lz52rcuHFq0aKF7rzzTo0ePVovvviifv/9d23evFnr169Xz549FRQUpHfffdf17J59K6xt5syZql27tubOnavY2FgtWrRI5cuX1/79++Xn56fMzEzl5ORIyrtpeUZGhqS8/wOQ3/5XNptN1NoAAACA5/j4+Cg3N7fY42RnZ0uScnNzdfToUadlmZmZCg0NVUZGhmOu/MJPknbu3On4nn/27FlJ/9urd/ToUQUFBalHjx5atWqV7Ha7Nm7cqIMHD8rf31+ZmZlauXKl7rvvPkl5exbXr1/vVnaO5XFD+fLlVa5cOdntdkVGRsrPz0/79u1TtWrVlJ6eripVqiggIEB+fn6qUaOGpLyCr0yZMo5DJ202m+OQxwoVKjjGPn8Xcf5hkOe3cdgVAAAA4BpPFHnnS0lJcRR950tKSpL0vwIuNzfX8fzQoUMXHPPcuXNavny5rrvuOs2bN0/GGP3666/KzMzUuHHj1KxZMz3xxBNas2aNPv74Yx07dsytzFQPxZCdna3s7GwdPHhQxhgdPXpUGRkZys7O1r59+yRJGRkZSklJUW5urtLT02WMUVZWliTp9OnTjg/C+Xv1fvvttwJtnv6wAgAAAMhT2LUA8ne62Gw2BQYGFmi/ELvd7vj+nn+Ip81mU1hYmGMHTlBQkMLDw3Xw4EEtWrRIubm58vHx0RdffKGbbrpJ77//vux2u4YPH66BAwe6f20Ct3rDSf4vLzw8XFLeRUoCAgIkSW3btpWUtxfwr/JP5ixTpoyjzcontAIAAADerLC9dcYY+fr6KigoSOnp6Y726tWrS5KjeJPkKAT9/f1lt9uVlZXlWJaZmSmTd7cDnThxwlFDnDt3TvXr11eTJk302WefKTc3V7m5uYqOjtbmzZv11ltvyd/fX3v27FHZsmV19dVXu7VNFHrFkH+ly/OLNH9/fwUEBKhy5cqS8j40+X38/Pzk4+PjtGs33/l77zhMEwAAACh5FStWdDwPDg4usNwYo7S0NKe2/NOvypUr5/gOn18I5ubmOo7ea9SokSTp1ltvVYsWLST9b0dP/pXzDx065Hiek5OjKlWqOK7WmX8F/aysLH300Ufq1q2bW9vGxViKwWazqVGjRtqzZ4+CgoJ08uRJ+fn56aabbtLSpUtlt9uVmpoqKe+DcObMGceVe6S8Kr4wHKYJAAAAlLxTp045nv+1oJMK/17+/fffS8o7b++vzt8z+Msvv0jKuxDLX2+NkL/uoUOH5Ofn56gR2rRpo08++UQ7duzQggUL1LJlS3Xp0kW5ubkaO3asW9tGoVdM1113nf744w+dPHlSubm5yszM1Pr162W3251+0WfOnJFU+G5hAAAAANaSv1Mnv8iz2WyOnUCZmZmy2Wzy8fHR/v37ZYxRs2bNtHXrVi1dutRxUZezZ8+qS5cu+s9//qPQ0FC35uc+egAAAABgMZwMBgAAAAAWw6GbXmjKlCmaMmWKMjMzHSdzAgAAAPAefn5+jivu33vvvZo7d24pJ3LGoZte6NSpUzp16pSSkpL0008/KScnR2fPnlVqaqoyMzMdl22tXLmycnJyHG35PyU5teU/srKyHBeMyV8WHBzsWKdKlSoF1vX393dcSfTMmTN/O1dR/f39/XXu3DmdPHlSp06dUm5urrKzs5WRkaHMzExlZGQoICBAPj4+8vPzU05Ojmw2m6NPQECAfH19ndryx8jKylJaWppj3ezsbAUGBiogIEB2u13+/v6OS9wGBAQ4xsjvn5qa6rgqav5cF+p/fraLHeP8/n9tO7+/J8cwxlywf9myZXXu3LlijVEauUtizr8bIzMzU9nZ2Tp37pyysrIcGbOzs+Xv768yZcrIGCO73e70uT7/s17U57qo/u78bVzsGOfOndO5c+eUkZEhKe+c4vwx/P39Va5cOWVnZysoKMhrfld8rq2f21t+x57+t/9S/ffm78bw1t/7pRijJP57fSk+ryXxmS+p33FOTo6Cg4MVGBioMmXKyG63y263q1y5co5bENjtdsfVLtPS0i7Ylv9TUoE2T/R3dYzg4GBVqFBBZcuW1VVXXSVJCgkJUVhYWEmVBxeFQg8AAAAALIZz9AAAAADAYij0AAAAAMBiKPQAAAAAwGIo9AAAAADAYij0AAD4GxMnTlSzZs1KOwYAAC6j0AMAWN7x48f16KOP6uqrr1ZAQICqV6+uO++8U2vXri3taAAAlAhumA4AsLSDBw+qVatWCg0N1QsvvKAmTZooKytLq1at0rBhw7R3797SjggAgMexRw8AYGmPPPKIbDabtmzZop49e6pevXpq1KiRRo8erU2bNkmSDh8+rG7duqls2bIKCQlR7969lZiYWOSYbdu21ciRI53aunfvrvvvv9/xulatWnr22WfVv39/lS1bVjVr1tSyZcv0xx9/OOZq2rSpvvvuO8c6CxYsUGhoqFatWqUGDRqobNmy6tSpk44dO+bo8+WXX+qmm25SmTJlFBoaqlatWunQoUOeebMAAJZBoQcAsKxTp04pPj5ew4YNU5kyZQosDw0NVW5urrp166ZTp07pq6++0po1a/Trr7/qH//4R7Hnnz59ulq1aqXt27erS5cuuu+++9S/f3/de++92rZtm2rXrq3+/fvLGONYJy0tTS+++KL+85//6Ouvv9bhw4f1r3/9S5KUnZ2t7t27q02bNtq5c6cSEhI0dOhQ2Wy2YmcFAFgLh24CACxr//79Msaofv36RfZZu3atdu3apQMHDqh69eqSpHfeeUeNGjXSt99+qxtvvPGi57/jjjv04IMPSpLGjx+v1157TTfeeKN69eolSXr88ccVHR2txMREhYeHS5KysrI0d+5c1a5dW5I0fPhwTZ48WZKUkpKi5ORkde3a1bG8QYMGF50PAGBd7NEDAFjW+XvKivLjjz+qevXqjiJPkho2bKjQ0FD9+OOPxZq/adOmjudVqlSRJDVp0qRA24kTJxxtwcHBjiJOkiIiIhzLK1asqPvvv18xMTG68847NXPmTKfDOgEAyEehBwCwrLp168pms3n8gis+Pj4FisisrKwC/ex2u+N5/uGVhbXl5uYWuk5+n/Pnmj9/vhISEnTzzTdr8eLFqlevnuNcQwAA8lHoAQAsq2LFioqJidGcOXOUmppaYHlSUpIaNGigI0eO6MiRI472PXv2KCkpSQ0bNix03MqVKzvtScvJydEPP/zg+Q0ownXXXadx48Zp48aNaty4seLi4i7Z3ACAywOFHgDA0ubMmaOcnBzddNNN+uijj7Rv3z79+OOPeuWVVxQdHa327durSZMmio2N1bZt27Rlyxb1799fbdq00Q033FDomLfddptWrFihFStWaO/evXr44YeVlJRU4tty4MABjRs3TgkJCTp06JBWr16tffv2cZ4eAKAALsYCALC0q6++Wtu2bdNzzz2nxx57TMeOHVPlypXVvHlzvfbaa7LZbPr000/16KOPqnXr1vLx8VGnTp00a9asIsd84IEH9P3336t///7y8/PTqFGj1K5duxLfluDgYO3du1cLFy7Un3/+qYiICA0bNsxxwRcAAPLZjCtnqgMAAAAALhscugkAAAAAFkOhBwAAAAAWQ6EHAAAAABZDoQcAAAAAFkOhBwAAAAAWQ6EHAAAAABZDoQcAAAAAFkOhBwAAAAAWQ6EHAAAAABZDoQcAAAAAFkOhBwAAAAAW8/8B8bwVRNhCgyAAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "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W5WYmOjW613MvffeqxkzZuiuu+7Sgw8+qIyMDL366qv69ttv9dVXXyk0NNSt7X4h27dv15///Gfdd999GjBggKZPn65bb71VaWlp6tKliyTrtMYOHTpo3759uvfee1WjRg2tXLlSY8eO1YEDBzR58mSXZU6fPl25ubm65557FB4erooVK9pa77Nnz+rnn39WhQoVnNPc2f8l6ZprrtGcOXOUnZ2t6OhoGWP01VdfKSgoSMuXL1fv3r0lScuXL1dQUJDatWtnqzYApYQBgFLm+PHjRpK58cYb3Rq/YcMGI8kMHjzYZfrf/vY3I8ksWrTIOU2SGTduXLFlJCUlmQEDBjgfT58+3UgyKSkpprCw0Dl95MiRJjg42GRlZTmnNWnSxHTo0MGtWj/99FMjyTz99NMu02+55RbjcDjMjh07nNM6dOhgmjRp4tZyfzu2devWZtCgQcYYY44dO2bCwsLMzJkzzeLFi40k88EHHxRbz4yMDGOMMZ988omRZL7++uvzvtbw4cNNdHS0OXv27HnHFL3W4sWLXWqUZN5++23ntLy8PBMfH2/69u3rnPaPf/zDSDKffvqpc9rp06dNw4YNiy3zXM6ePWsSEhJMcnKyy/Rp06YZSWb+/PnGGGNyc3NNQUGBy5iMjAwTHh5unnzySZdpksz06dNd1uVcPR8wYIBJSkpyPl6+fLmRZGbNmuUyLi0tzWW6O9v9fJKSkowk89FHHzmnHT9+3CQkJJiWLVs6pz311FOmTJky5scff3R5/v/93/+Z4OBgs3fvXpf1jY6ONocOHXK7hq5du5rDhw+bw4cPm02bNpk77rjDSDJDhw51jnN3///666+NJDNv3jxjjDEbN240ksytt95q2rZt63xe7969XdYRAH6LU/sAlDrZ2dmSpHLlyrk1ft68eZKkUaNGuUwvuvD9j1xLdc8998jhcDgfX3PNNSooKNCePXsuaXnz5s1TcHCwHnzwwWK1GmM8corS7bffro8//lhnzpzRhx9+qODgYN18881uPbfomqy5c+cqPz//vGNOnTql9PR027WVLVvW5TqasLAwtWnTRrt27XJOS0tLU9WqVZ1HHSTrRhruXmcTHBysfv36adWqVS6nLM6ePVtxcXHq3LmzJCk8PFxBQdav2YKCAh05ckRly5ZVgwYN9M0339het3P54IMPVL58eXXp0kW//PKL86tVq1YqW7as8yibO9v9QhITE116HB0drTvvvFPffvutMjMznbVcc801qlChgkstKSkpKigo0LJly1yW2bdvX1WpUsXtGr788ktVqVJFVapUUbNmzfSf//xHd911l55//nnnGHf3/5YtW6ps2bLOmpYvX65q1arpzjvv1DfffKOcnBwZY7RixQpdc8019jYWgFKDIAWg1ImOjpakC97C+rf27NmjoKAg1a1b12V6fHy8YmJiLjn0SFKNGjVcHhedpvT761vctWfPHiUmJhYLiUWn7f2RWov069dPx48f1xdffKFZs2bp+uuvdzuUdujQQX379tWECRNUuXJl3XjjjZo+fbrLtWZ//etfVb9+ffXo0UPVqlXT3XffrbS0NLeWX61aNZdgKlnb9Lfbc8+ePapTp06xcb/v74UU3Uxi9uzZkqSff/5Zy5cvV79+/Zw31ygsLNRLL72kevXqKTw8XJUrV1aVKlW0ceNGHT9+3O3XupDt27fr+PHjio2NdYaMoq+TJ086r+NyZ7tfSN26dYttr/r160uSM0xu375daWlpxepISUmRpGLXlNWqVcvWurZt21bp6elKS0vTCy+8oJiYGB07dszlBhXu7v/BwcFKTk7W8uXLJVlB6pprrlH79u1VUFCg1atXa+vWrTp69ChBCsB5cY0UgFInOjpaiYmJ2rx5s63n/f6NpB0FBQXnnH6+O9qZ31wY72sSEhLUsWNH/eMf/9BXX31V7E59F1L0OVOrV6/W559/rvnz5+vuu+/WP/7xD61evVply5ZVbGysNmzYoPnz5+uLL77QF198oenTp+vOO+/UzJkzL7j8y7U9W7VqpYYNG+rdd9/VI488onfffVfGGJe79T377LN6/PHHdffdd+upp55SxYoVFRQUpBEjRrjcfOFcHA7HOWv+/X5UWFio2NhYzZo165zLKTri4852/6MKCwvVpUsXjRkz5pzzi4JXkcjISFvLr1y5sjOUdevWTQ0bNtT111+vl19+udjRYne0b99ezzzzjHJzc7V8+XI9+uijiomJUdOmTbV8+XLntYgEKQDnQ5ACUCpdf/31ev3117Vq1SolJydfcGxSUpIKCwu1fft2lxsyHDx4UFlZWUpKSnJOq1ChgrKyslyef+bMGR04cOCSa7UT4JKSkrRgwQKdOHHC5a/yP/zwg3O+J9x+++0aPHiwYmJi1LNnT9vPv+qqq3TVVVfpmWee0ezZs5Wamqr33ntPgwcPlmSdknfDDTfohhtuUGFhof7617/qX//6lx5//HFbR47OJSkpSVu3bpUxxmXb7tixw9ZyUlNT9fjjj2vjxo2aPXu26tWrpyuvvNI5/8MPP1SnTp305ptvujwvKytLlStXvuCyK1So4HI6YpHfH1GsU6eOFixYoHbt2rkVTC623c9nx44dxbbXjz/+KEnOuwjWqVNHJ0+edIadktarVy916NBBzz77rO69916VKVPG1v5/zTXX6MyZM3r33Xe1b98+Z2C69tprnUGqfv36F7y5C4DSjVP7AJRKY8aMUZkyZTR48GAdPHiw2PydO3c6b7ddFBR+f9exF198UZL1hq5InTp1il0L8vrrr5/3iJQ7ypQpUyycnU/Pnj1VUFCgV1991WX6Sy+9JIfD4bxz3R91yy23aNy4cXrttddsfSjusWPHih1padGihSQ5TzM7cuSIy/ygoCBdccUVLmP+iG7dumnfvn0ut7nOzc3VG2+8YWs5RUefnnjiCW3YsKHYZ0cFBwcXW9cPPvhA+/btu+iy69Spox9++MHlVvjfffedvvrqK5dxt912mwoKCvTUU08VW8bZs2ed+4072/1C9u/f73J3yuzsbL399ttq0aKF4uPjnbWsWrVK8+fPL/b8rKwsnT179qKvY9fDDz+sI0eOOHtnZ/9v27atQkND9dxzz6lixYpq0qSJJCtgrV69WkuXLuVoFIAL4ogUgFKpTp06mj17tv785z+rUaNGuvPOO9W0aVOdOXNGK1eu1AcffOD83KfmzZtrwIABev3115WVlaUOHTpo7dq1mjlzpm666SZ16tTJudzBgwfrvvvuU9++fdWlSxd99913mj9//kWPQFxIq1atNHXqVD399NOqW7euYmNjnbce/70bbrhBnTp10qOPPqrdu3erefPm+vLLLzVnzhyNGDFCderUueQ6fqt8+fLn/Lysi5k5c6Zee+013XzzzapTp45OnDihN954Q9HR0c7AOnjwYB09elTXXXedqlWrpj179uiVV15RixYt3LpF+8Xce++9evXVV9W/f38NHz5cCQkJmjVrlvMDft09AlirVi1dffXVmjNnjiQVC1LXX3+9nnzySd111126+uqrtWnTJs2aNUu1a9e+6LLvvvtuvfjii+rWrZsGDRqkQ4cO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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5) Visualising the Scale of the Features (by looking at the difference between the minimum and maximum values) using a range of different plots"
      ],
      "metadata": {
        "id": "rp8LM7_myAlh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "########Scales#########\n",
        "# Calculate maxima and minima\n",
        "maxima = feature_variables.max()\n",
        "minima = feature_variables.min()\n",
        "\n",
        "# Convert maxima and minima to vectors\n",
        "maxima_vector = maxima.values\n",
        "minima_vector = minima.values\n",
        "\n",
        "# Plot maxima and minima vectors\n",
        "plt.plot(maxima_vector, label='Maxima', marker='o', linestyle = \"none\")\n",
        "plt.plot(minima_vector, label='Minima', marker='x', linestyle = \"none\")\n",
        "\n",
        "# Add labels and legend\n",
        "plt.xlabel('Feature Index')\n",
        "plt.ylabel('Values')\n",
        "plt.title('Maxima and Minima of Variables')\n",
        "plt.legend()\n",
        "\n",
        "# Show plot\n",
        "plt.show()\n",
        "\n",
        "\n",
        "###### BoxPlots#####\n",
        "\n",
        "# Calculate ranges for each variable\n",
        "ranges = feature_variables.max() - feature_variables.min()\n",
        "\n",
        "########BAR PLOT#######\n",
        "\n",
        "plt.figure()\n",
        "plt.bar(ranges.index, ranges.values)\n",
        "plt.xlabel('Columns')\n",
        "plt.ylabel('Range')\n",
        "plt.title('Ranges of Columns')\n",
        "\n",
        "\n",
        "\n",
        "# Plot histogram of ranges\n",
        "plt.figure()\n",
        "plt.hist(ranges, edgecolor='black', alpha=0.7)\n",
        "plt.xlabel('Range')\n",
        "plt.ylabel('Frequency')\n",
        "plt.title('Histogram of Variable Ranges')\n",
        "\n",
        "# Show plot\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "KX77R6frwaeM",
        "outputId": "7b2f8ea5-929d-4ebd-82ee-6ddeb6b0ece9"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkAAAAHHCAYAAABXx+fLAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABPZ0lEQVR4nO3deVxU9f4/8NcZZIcZZIcE91xCzZUw1zRB0dzKVLyCet3C3DLNcrdErcxcyqwrlEmWhnm1q37NBTXJXHONlFRcQBQEBGSdz+8PfpwY2QYYGPC8no/HPJw553M+530+c2BennPmIAkhBIiIiIgURGXsAoiIiIiqGwMQERERKQ4DEBERESkOAxAREREpDgMQERERKQ4DEBERESkOAxAREREpDgMQERERKQ4DEBERESkOAxBRFZEkCYsWLTJ2GdXu8OHDkCQJhw8frrJ1VGZsGzRogKCgIIPWU1327t2L559/HhYWFpAkCcnJycYuqVLvd1BQEGxsbPRqq9SfJ6o6DED0VAkLC4MkSZAkCceOHSsyXwgBDw8PSJKE/v37G6FCKsD3qnwSExMxbNgwWFpaYv369di8eTOsra2LtHvllVdgZWWFR48eldhXQEAAzMzMkJiYWJUlE9VodYxdAFFVsLCwQHh4OLp06aIzPTIyErdv34a5uXmV1/D48WPUqcMfsbJU5L2qzNhGR0dDpap9//c7efIkHj16hKVLl6J3794ltgsICMCuXbuwY8cOjB49usj8jIwM7Ny5E35+fnBwcKh0Xd26dcPjx49hZmZW6b6IqlPt+y1ApId+/fph27ZtyM3N1ZkeHh6O9u3bw9XVtcprsLCwYADSQ0Xeq8qMrbm5OUxNTSu0rDElJCQAAOzs7Ept98orr8DW1hbh4eHFzt+5cyfS09MREBBQqXoyMzOh1WqhUqlgYWFRK0MlKRv3WHoqjRgxAomJidi/f788LTs7G9u3b8fIkSOLXeajjz5C586d4eDgAEtLS7Rv3x7bt2/XaRMaGgpJkrBp0yad6cuWLYMkSfjf//4nT3vymoVFixZBkiT89ddfGDVqFDQaDZycnDB//nwIIXDr1i0MHDgQarUarq6u+Pjjj3XWkZ2djQULFqB9+/bQaDSwtrZG165dcejQIb3GZOfOnfD394e7uzvMzc3RuHFjLF26FHl5eTrtevToAS8vL1y+fBk9e/aElZUVnnnmGaxcubJIn7dv38agQYNgbW0NZ2dnzJgxA1lZWXrVU6Ai71VJY3vt2jUEBQXBzs4OGo0GY8aMQUZGhs6yT14DVHAq7tixY5g6dSqcnJxgZ2eHiRMnIjs7G8nJyRg9ejTq1q2LunXrYvbs2RBC6PSpz75Tmm3btqF9+/awtLSEo6MjRo0ahTt37sjze/TogcDAQABAx44dIUlSidcxWVpaYsiQIThw4IAcmgoLDw+Hra0tXnnlFSQlJWHWrFlo1aoVbGxsoFar0bdvX/zxxx86yxRc57N161bMmzcPzzzzDKysrJCamlrsNUBHjx7Fa6+9Bk9PT5ibm8PDwwMzZszA48ePi63577//hq+vL6ytreHu7o4lS5YUGePi3LlzB2PHjoWLiwvMzc3x3HPPFfnZBIC1a9fiueeeg5WVFerWrYsOHTqUGBBJORiA6KnUoEED+Pj44LvvvpOn7dmzBykpKRg+fHixy3z66ado27YtlixZgmXLlqFOnTp47bXX8PPPP8ttxowZg/79+2PmzJm4desWAODChQtYvHgxxo0bh379+pVZ2+uvvw6tVovly5fD29sb77//PlavXo2XX34ZzzzzDFasWIEmTZpg1qxZOHLkiLxcamoqvvrqK/To0QMrVqzAokWLcP/+ffj6+uLcuXNlrjcsLAw2NjaYOXMmPv30U7Rv3x4LFizAO++8U6Ttw4cP4efnhzZt2uDjjz9G8+bNMWfOHOzZs0du8/jxY/Tq1Qv79u3DlClT8N577+Ho0aOYPXt2mbUUVpH3qiTDhg3Do0ePEBISgmHDhiEsLAyLFy/Wa9k333wTV69exeLFi/HKK69g48aNmD9/PgYMGIC8vDwsW7YMXbp0wYcffojNmzfrLKvPvlOSsLAwDBs2DCYmJggJCcH48eMRERGBLl26yBc5v/fee5gwYQIAYMmSJdi8eTMmTpxYYp8BAQHIzc3FDz/8oDM9KSkJ+/btw+DBg2FpaYm///4bP/30E/r3749Vq1bh7bffxoULF9C9e3fcvXu3SL9Lly7Fzz//jFmzZmHZsmUlnvbatm0bMjIyMHnyZKxduxa+vr5Yu3Ztsafk8vLy4OfnBxcXF6xcuRLt27fHwoULsXDhwlLH7d69e3jhhRfwyy+/YMqUKfj000/RpEkTjBs3DqtXr5bbffnll5g6dSpatmyJ1atXY/HixXj++edx4sSJUvsnBRBET5HQ0FABQJw8eVKsW7dO2NraioyMDCGEEK+99pro2bOnEEKI+vXrC39/f51lC9oVyM7OFl5eXuKll17SmR4XFyfs7e3Fyy+/LLKyskTbtm2Fp6enSElJ0WkHQCxcuFB+vXDhQgFATJgwQZ6Wm5sr6tWrJyRJEsuXL5enP3z4UFhaWorAwECdtllZWTrrePjwoXBxcRFjx44tc2ye3D4hhJg4caKwsrISmZmZ8rTu3bsLAOKbb76Rp2VlZQlXV1cxdOhQedrq1asFAPHDDz/I09LT00WTJk0EAHHo0KFS66nMe1XS2D45DoMHDxYODg460+rXr68zrgV1+Pr6Cq1WK0/38fERkiSJSZMmydMK3q/u3bvr9KnvvvOk7Oxs4ezsLLy8vMTjx4/l6bt37xYAxIIFC4rUefLkyVL7LKjTzc1N+Pj46EzfsGGDACD27dsnhBAiMzNT5OXl6bS5fv26MDc3F0uWLJGnHTp0SAAQjRo1KrKtBfMKv9/F7WshISFCkiRx8+ZNeVpgYKAAIN588015mlarFf7+/sLMzEzcv39fnv7kez5u3Djh5uYmHjx4oLOe4cOHC41GI9cwcOBA8dxzzxU7TqRsPAJET61hw4bh8ePH2L17Nx49eoTdu3eXeEoFyD91UODhw4dISUlB165dcebMGZ12rq6uWL9+Pfbv34+uXbvi3Llz2LRpE9RqtV51/fvf/5afm5iYoEOHDhBCYNy4cfJ0Ozs7NGvWDH///bdO24L/cWu1WiQlJSE3NxcdOnQoUmNZ2/fo0SM8ePAAXbt2RUZGBv7880+dtjY2Nhg1apT82szMDJ06ddKp53//+x/c3Nzw6quvytOsrKzkIxXlUd73qiSTJk3Sed21a1ckJiYiNTW1zGXHjRsHSZLk197e3kXel4L3q/A4APrvO086deoUEhIS8MYbb8DCwkKe7u/vj+bNm+t1BKk4JiYmGD58OKKionDjxg15enh4OFxcXNCrVy8A+ddDFVy7k5eXh8TERNjY2KBZs2bF1h4YGKizrSUp3CY9PR0PHjxA586dIYTA2bNni7SfMmWK/FySJEyZMgXZ2dn45Zdfiu1fCIEff/wRAwYMgBACDx48kB++vr5ISUmR67ezs8Pt27dx8uTJMusmZWEAoqeWk5MTevfujfDwcERERCAvL0/nw/pJu3fvxgsvvAALCwvY29vDyckJn3/+OVJSUoq0HT58OPz9/fH7779j/Pjx8geKPjw9PXVeazQaWFhYwNHRscj0hw8f6kz7+uuv0bp1a1hYWMDBwQFOTk74+eefi63xSZcuXcLgwYOh0WigVqvh5OQkh5wnl69Xr55OGACAunXr6tRz8+ZNNGnSpEi7Zs2alVnLk8r7XpXkybGtW7cuABQZR32W1Wg0AAAPD48i05/srzz7TmE3b94EUPyYNW/eXJ5fEQUXORdc63L79m0cPXoUw4cPh4mJCYD8IP3JJ5+gadOmMDc3h6OjI5ycnHD+/Plia2/YsKFe646NjUVQUBDs7e1hY2MDJycndO/eHUDRfU2lUqFRo0Y605599lkA0Alvhd2/fx/JycnYuHEjnJycdB5jxowB8M9F43PmzIGNjQ06deqEpk2bIjg4GL/++qte20FPN35FhZ5qI0eOxPjx4xEfH4++ffuW+A2ao0eP4pVXXkG3bt3w2Wefwc3NDaampggNDS32YsnExEScOnUKAHD58mX52zD6KPjwKWsaAJ0LQb/99lsEBQVh0KBBePvtt+Hs7CxfNxITE1PqOpOTk9G9e3eo1WosWbIEjRs3hoWFBc6cOYM5c+ZAq9WWux5D0/e9Kk1l6i5p2eKmF+6vvPtOdWnfvj2aN2+O7777Du+++y6+++47CCF0vv21bNkyzJ8/H2PHjsXSpUthb28PlUqF6dOnF9knAOh19CcvLw8vv/wykpKSMGfOHDRv3hzW1ta4c+cOgoKCiu23vAr6GDVqlHxx+JNat24NAGjRogWio6Oxe/du7N27Fz/++CM+++wzLFiwQO/rw+jpxABET7XBgwdj4sSJ+O233/D999+X2O7HH3+EhYUF9u3bp3PfmdDQ0GLbBwcHyxfbzp07F6tXr8bMmTMNXn9h27dvR6NGjRAREaFz1KWsi0WB/G/xJCYmIiIiAt26dZOnX79+vcL11K9fHxcvXoQQQqee6OjoCvWn73tV05R33ymsfv36APLH7KWXXtKZFx0dLc+vqICAAMyfPx/nz59HeHg4mjZtio4dO8rzt2/fjp49e+I///mPznLJyclFjkjq68KFC/jrr7/w9ddf61z0XPhbfoVptVr8/fff8lEfAPjrr78A5F8gXxwnJyfY2toiLy+v1HsiFbC2tsbrr7+O119/HdnZ2RgyZAg++OADzJ07V+fUIykLT4HRU83Gxgaff/45Fi1ahAEDBpTYzsTEBJIk6Xwl/MaNG/jpp5+KtN2+fTu+//57LF++HO+88w6GDx+OefPmyb+0q0rBkYjCRx9OnDiBqKioCi2bnZ2Nzz77rML19OvXD3fv3tX5undGRgY2btxYof70fa9qmvLsO0/q0KEDnJ2dsWHDBp3bB+zZswdXrlyBv79/pWorONqzYMECnDt3rsi9f0xMTIocHdu2bZvOV/DLq7h9TQiBTz/9tMRl1q1bp9N23bp1MDU1LfHUsomJCYYOHYoff/wRFy9eLDL//v378vMn73ZtZmaGli1bQgiBnJwc/TaKnko8AkRPvZIOkRfm7++PVatWwc/PDyNHjkRCQgLWr1+PJk2a4Pz583K7hIQETJ48GT179pQv3Fy3bh0OHTqEoKAgHDt2rMpuCNe/f39ERERg8ODB8Pf3x/Xr17Fhwwa0bNkSaWlppS7buXNn1K1bF4GBgZg6dSokScLmzZsrdUpr/PjxWLduHUaPHo3Tp0/Dzc0NmzdvhpWVVYX71Oe9qmn03XeKY2pqihUrVmDMmDHo3r07RowYgXv37uHTTz9FgwYNMGPGjErV1rBhQ3Tu3Bk7d+4EgCIBqH///liyZAnGjBmDzp0748KFC9iyZUuRa3LKo3nz5mjcuDFmzZqFO3fuQK1W48cffyzxOiwLCwvs3bsXgYGB8Pb2xp49e/Dzzz/j3XffhZOTU4nrWb58OQ4dOgRvb2+MHz8eLVu2RFJSEs6cOYNffvkFSUlJAIA+ffrA1dUVL774IlxcXHDlyhWsW7cO/v7+sLW1rfB2Uu3HI0BEAF566SX85z//QXx8PKZPn47vvvsOK1aswODBg3XaTZ48GVlZWfINEQHAwcEBGzduRFRUFD766KMqqzEoKAjLli3DH3/8galTp2Lfvn349ttv0aFDhzKXdXBwwO7du+Hm5oZ58+bho48+wssvv1zszQ31ZWVlhQMHDqBPnz5Yu3Yt3n//fXTp0qVSfdZG+u47JQkKCsL333+P7OxszJkzB1988QUGDx6MY8eOVeg6qCcVhJ5OnTqhSZMmOvPeffddvPXWW9i3bx+mTZuGM2fO4Oeffy5y4Xd5mJqaYteuXXj++ecREhKCxYsXo2nTpvjmm2+KbW9iYoK9e/ciPj4eb7/9Nk6ePImFCxdi6dKlpa7HxcUFv//+O8aMGYOIiAj5XkBJSUlYsWKF3G7ixIlIS0vDqlWrEBwcjJ9++glTp07Ft99+W+FtpKeDJKryqkYiIiKiGohHgIiIiEhxGICIiIhIcRiAiIiISHEYgIiIiEhxGICIiIhIcRiAiIiISHF4I0Tk34r97t27sLW1LfKHHYmIiKhmEkLg0aNHcHd3L/dNaBmAANy9e7dSN/4iIiIi47l16xbq1atXrmUYgAD5dui3bt2CWq02cjVERESkj9TUVHh4eFToz5owAAHyaS+1Ws0AREREVMtU5PIVXgRNREREisMARERERIrDAERERESKw2uAiIiIAOTl5SEnJ8fYZVAhpqamMDExqZK+GYCIiEjRhBCIj49HcnKysUuhYtjZ2cHV1dXg9+ljACIiIkUrCD/Ozs6wsrLiDXFrCCEEMjIykJCQAABwc3MzaP8MQEREpFh5eXly+HFwcDB2OfQES0tLAEBCQgKcnZ0NejqMF0ETEZFiFVzzY2VlZeRKqCQF742hr89iACIiIsXjaa+aq6reG54CqyJ5WoHfrych4VEmnG0t0KmhPUxU/AEjIiKqCRiAqsDei3FYvOsy4lIy5WluGgssHNASfl6GvYiLiIioOjRo0ADTp0/H9OnTjV2KQfAUmIHtvRiHyd+e0Qk/ABCfkonJ357B3otxRqqMiIiqSp5WIComETvP3UFUTCLytKLK1xkUFARJkjBp0qQi84KDgyFJEoKCggy2vpMnT2LChAkG68/YeATIgPK0Aot3XUZxu70AIAFYvOsyXm7pytNhRERPCWMe9ffw8MDWrVvxySefyN+YyszMRHh4ODw9PQ26LicnJ4P2Z2w8AmRAv19PKnLkpzABIC4lE79fT6q+ooiIqMoY+6h/u3bt4OHhgYiICHlaREQEPD090bZt23/q3LsXXbp0gZ2dHRwcHNC/f3/ExMTI87/55hvY2Njg6tWr8rQ33ngDzZs3R0ZGBoD8U2CrV6+W50uShC+++AL9+/eHlZUVWrRogaioKFy7dg09evSAtbU1OnfurLOemJgYDBw4EC4uLrCxsUHHjh3xyy+/VMXQlIkByIASHpUcfirSjoiIaq6yjvoD+Uf9q/p02NixYxEaGiq/3rRpE8aMGaPTJj09HTNnzsSpU6dw4MABqFQqDB48GFqtFgAwevRo9OvXDwEBAcjNzcXPP/+Mr776Clu2bCn1FgFLly7F6NGjce7cOTRv3hwjR47ExIkTMXfuXJw6dQpCCEyZMkVun5aWhn79+uHAgQM4e/Ys/Pz8MGDAAMTGxhp4VMrGAGRAzrYWBm1HREQ1V0056j9q1CgcO3YMN2/exM2bN/Hrr79i1KhROm2GDh2KIUOGoEmTJnj++eexadMmXLhwAZcvX5bbfPHFF4iLi8PUqVMxbtw4LFq0CO3bty913WPGjMGwYcPw7LPPYs6cObhx4wYCAgLg6+uLFi1aYNq0aTh8+LDcvk2bNpg4cSK8vLzQtGlTLF26FI0bN8Z///tfg46JPhiADKhTQ3u4aSxQ0tU9EvLPC3dqaF+dZRERURWoKUf9nZyc4O/vj7CwMISGhsLf3x+Ojo46ba5evYoRI0agUaNGUKvVaNCgAQDoHHmpW7cu/vOf/+Dzzz9H48aN8c4775S57tatW8vPXVxcAACtWrXSmZaZmYnU1FQA+UeAZs2ahRYtWsDOzg42Nja4cuWKUY4A8SJoAzJRSVg4oCUmf3sGEqBzWLQgFC0c0JIXQBMRPQVq0lH/sWPHyqea1q9fX2T+gAEDUL9+fXz55Zdwd3eHVquFl5cXsrOzddodOXIEJiYmiIuLQ3p6OmxtbUtdr6mpqfy84IaFxU0rONU2a9Ys7N+/Hx999BGaNGkCS0tLvPrqq0XqqA48AmRgfl5u+HxUO7hqdHd4V40FPh/VjvcBIiJ6StSko/5+fn7Izs5GTk4OfH19deYlJiYiOjoa8+bNQ69evdCiRQs8fPiwSB/Hjx/HihUrsGvXLtjY2Ohcu2Mov/76K4KCgjB48GC0atUKrq6uuHHjhsHXow8eAaoCfl5ueLmlK+8ETUT0FKtJR/1NTExw5coV+XlhdevWhYODAzZu3Ag3NzfExsYWOb316NEj/Otf/8LUqVPRt29f1KtXDx07dsSAAQPw6quvGqzOpk2bIiIiAgMGDIAkSZg/f758dKi68QhQFTFRSfBp7ICBzz8Dn8YODD9ERE+hmnTUX61WQ61WF5muUqmwdetWnD59Gl5eXpgxYwY+/PBDnTbTpk2DtbU1li1bBiD/Op5ly5Zh4sSJuHPnjsFqXLVqFerWrYvOnTtjwIAB8PX1Rbt27QzWf3lIQoiqv11lDZeamgqNRoOUlJRidx4iIno6ZWZm4vr162jYsCEsLCp+rQ7//mPVKe09qsznN0+BERERVVLBUX+qPXgKjIiIiBSHAYiIiIgUhwGIiIiIFIcBiIiIiBSHAYiIiIgUhwGIiIiIFIcBiIiIiBSHAYiIiIgUhwGIiIjoKdejRw9Mnz5d7/Y3btyAJEk4d+5cldVkbAxAREREtVBQUBAkScKkSZOKzAsODoYkSQgKCgIAREREYOnSpXr37eHhgbi4OHh5eRmq3BqHAYiIiKiiDoUAkSuLnxe5Mn9+FfLw8MDWrVvx+PFjeVpmZibCw8Ph6ekpT7O3t4etra3e/ZqYmMDV1RV16jy9fzGLAYiIiKiiVCbAoQ+KhqDIlfnTVSZVuvp27drBw8MDERER8rSIiAh4enqibdu28rQnT4E1aNAAy5Ytw9ixY2FrawtPT09s3LhRnv/kKbDDhw9DkiTs27cPbdu2haWlJV566SUkJCRgz549aNGiBdRqNUaOHImMjAy5n71796JLly6ws7ODg4MD+vfvj5iYmKobkHJgACIiIqqo7rOBnu/phqCC8NPzvfz5VWzs2LEIDQ2VX2/atAljxowpc7mPP/4YHTp0wNmzZ/HGG29g8uTJiI6OLnWZRYsWYd26dTh+/Dhu3bqFYcOGYfXq1QgPD8fPP/+M//u//8PatWvl9unp6Zg5cyZOnTqFAwcOQKVSYfDgwdBqtRXfYAN5eo9tERERVYeCkHPoA+DIh0BedrWFHwAYNWoU5s6di5s3bwIAfv31V2zduhWHDx8udbl+/frhjTfeAADMmTMHn3zyCQ4dOoRmzZqVuMz777+PF198EQAwbtw4zJ07FzExMWjUqBEA4NVXX8WhQ4cwZ84cAMDQoUN1lt+0aROcnJxw+fJlo19fxCNAREREldV9NmBilh9+TMyqLfwAgJOTE/z9/REWFobQ0FD4+/vD0dGxzOVat24tP5ckCa6urkhISNB7GRcXF1hZWcnhp2Ba4T6uXr2KESNGoFGjRlCr1WjQoAEAIDY2Vt/NqzI8AkRERFRZkSv/CT952fmvqzEEjR07FlOmTAEArF+/Xq9lTE1NdV5LklTmqanCy0iSVGYfAwYMQP369fHll1/C3d0dWq0WXl5eyM7O1qvGqsQAREREVBlPXvNT8BqothDk5+eH7OxsSJIEX1/fallnWRITExEdHY0vv/wSXbt2BQAcO3bMyFX9gwGIiIioooq74LnwNUGFX1chExMTXLlyRX5eE9StWxcODg7YuHEj3NzcEBsbi3feecfYZckYgIiIiCpKm1f8Bc8Fr7V51VaKWq2utnXpQ6VSYevWrZg6dSq8vLzQrFkzrFmzBj169DB2aQAASQghjF2EsaWmpkKj0SAlJaXG7UBERFR1MjMzcf36dTRs2BAWFhbGLoeKUdp7VJnPb34LjIiIiBSHAYiIiIgUhwGIiIiIFIcBiIiIiBSHAYiIiBSP3wequarqvWEAIiIixSq4k3Hhv2BONUvBe/PkXacry6j3AQoJCUFERAT+/PNPWFpaonPnzlixYoXOH2Lr0aMHIiMjdZabOHEiNmzYIL+OjY3F5MmTcejQIdjY2CAwMBAhISGoU4e3OSIiopKZmJjAzs5O/vtVVlZWkCTJyFURkH/kJyMjAwkJCbCzszP4DR6NmhAiIyMRHByMjh07Ijc3F++++y769OmDy5cvw9raWm43fvx4LFmyRH5tZWUlP8/Ly4O/vz9cXV1x/PhxxMXFYfTo0TA1NcWyZcuqdXuIiKj2cXV1BYAy/xAoGYednZ38HhlSjboR4v379+Hs7IzIyEh069YNQP4RoOeffx6rV68udpk9e/agf//+uHv3LlxcXAAAGzZswJw5c3D//n2YmZmVuV7eCJGIiPLy8pCTk2PsMqgQU1PTUo/8VObzu0adI0pJSQEA2Nvb60zfsmULvv32W7i6umLAgAGYP3++fBQoKioKrVq1ksMPAPj6+mLy5Mm4dOkS2rZtW2Q9WVlZyMrKkl+npqZWxeYQEVEtYmJiUmP+jhZVvRoTgLRaLaZPn44XX3wRXl5e8vSRI0eifv36cHd3x/nz5zFnzhxER0cjIiICABAfH68TfgDIr+Pj44tdV0hICBYvXlxFW0JEREQ1XY0JQMHBwbh48SKOHTumM33ChAny81atWsHNzQ29evVCTEwMGjduXKF1zZ07FzNnzpRfp6amwsPDo2KFExERUa1TI74GP2XKFOzevRuHDh1CvXr1Sm3r7e0NALh27RqA/IvX7t27p9Om4HVJF02Zm5tDrVbrPIiIiEg5jBqAhBCYMmUKduzYgYMHD6Jhw4ZlLnPu3DkAgJubGwDAx8cHFy5c0Ll6f//+/VCr1WjZsmWV1E1ERES1m1FPgQUHByM8PBw7d+6Era2tfM2ORqOBpaUlYmJiEB4ejn79+sHBwQHnz5/HjBkz0K1bN7Ru3RoA0KdPH7Rs2RL/+te/sHLlSsTHx2PevHkIDg6Gubm5MTePiIiIaiijfg2+pJtNhYaGIigoCLdu3cKoUaNw8eJFpKenw8PDA4MHD8a8efN0TlvdvHkTkydPxuHDh2FtbY3AwEAsX75c7xsh8mvwREREtU9lPr9r1H2AjIUBiIiIqPapzOd3jbgImoiIiKg6MQARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIYNQCFhISgY8eOsLW1hbOzMwYNGoTo6GidNpmZmQgODoaDgwNsbGwwdOhQ3Lt3T6dNbGws/P39YWVlBWdnZ7z99tvIzc2tzk0hIiKiWsSoASgyMhLBwcH47bffsH//fuTk5KBPnz5IT0+X28yYMQO7du3Ctm3bEBkZibt372LIkCHy/Ly8PPj7+yM7OxvHjx/H119/jbCwMCxYsMAYm0RERES1gCSEEMYuosD9+/fh7OyMyMhIdOvWDSkpKXByckJ4eDheffVVAMCff/6JFi1aICoqCi+88AL27NmD/v374+7du3BxcQEAbNiwAXPmzMH9+/dhZmZW5npTU1Oh0WiQkpICtVpdpdtIREREhlGZz+8adQ1QSkoKAMDe3h4AcPr0aeTk5KB3795ym+bNm8PT0xNRUVEAgKioKLRq1UoOPwDg6+uL1NRUXLp0qdj1ZGVlITU1VedBREREylFjApBWq8X06dPx4osvwsvLCwAQHx8PMzMz2NnZ6bR1cXFBfHy83KZw+CmYXzCvOCEhIdBoNPLDw8PDwFtDRERENVmNCUDBwcG4ePEitm7dWuXrmjt3LlJSUuTHrVu3qnydREREVHPUMXYBADBlyhTs3r0bR44cQb169eTprq6uyM7ORnJyss5RoHv37sHV1VVu8/vvv+v0V/AtsYI2TzI3N4e5ubmBt4KIiIhqC6MeARJCYMqUKdixYwcOHjyIhg0b6sxv3749TE1NceDAAXladHQ0YmNj4ePjAwDw8fHBhQsXkJCQILfZv38/1Go1WrZsWT0bQkRERLWKUY8ABQcHIzw8HDt37oStra18zY5Go4GlpSU0Gg3GjRuHmTNnwt7eHmq1Gm+++SZ8fHzwwgsvAAD69OmDli1b4l//+hdWrlyJ+Ph4zJs3D8HBwTzKQ0RERMUy6tfgJUkqdnpoaCiCgoIA5N8I8a233sJ3332HrKws+Pr64rPPPtM5vXXz5k1MnjwZhw8fhrW1NQIDA7F8+XLUqaNfvuPX4ImIiGqfynx+16j7ABkLAxAREVHt89TcB4iIiIioOjAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4pQ7AN26dQu3b9+WX//++++YPn06Nm7caNDCiIiIiKpKuQPQyJEjcejQIQBAfHw8Xn75Zfz+++947733sGTJEoMXSERERGRo5Q5AFy9eRKdOnQAAP/zwA7y8vHD8+HFs2bIFYWFhhq6PiIiIyODKHYBycnJgbm4OAPjll1/wyiuvAACaN2+OuLg4w1ZHREREVAXKHYCee+45bNiwAUePHsX+/fvh5+cHALh79y4cHBwMXiARERGRoZU7AK1YsQJffPEFevTogREjRqBNmzYAgP/+97/yqTF9HTlyBAMGDIC7uzsk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BiAiIiJSHAYgIiIiUhwGICIiIlIcBiAiIiJSHAYgIiIiUhwGICIiIlIcBiAiIiJSHAYgIiIiUhwGICIiIlIcBiAiIiJSHAYgIiIiUhwGICIiIlIcowagI0eOYMCAAXB3d4ckSfjpp5905gshsGDBAri5ucHS0hK9e/fG1atXddokJSUhICAAarUadnZ2GDduHNLS0qpxK4iIiKi2MWoASk9PR5s2bbB+/fpi569cuRJr1qzBhg0bcOLECVhbW8PX1xeZmZlym4CAAFy6dAn79+/H7t27ceTIEUyYMKG6NoGIiIhqIUkIIYxdBABIkoQdO3Zg0KBBAPKP/ri7u+Ott97CrFmzAAApKSlwcXFBWFgYhg8fjitXrqBly5Y4efIkOnToAADYu3cv+vXrh9u3b8Pd3V2vdaempkKj0SAlJQVqtbpKto+IiIgMqzKf3zX2GqDr168jPj4evXv3lqdpNBp4e3sjKioKABAVFQU7Ozs5/ABA7969oVKpcOLEiRL7zsrKQmpqqs6DiIiIlKPGBqD4+HgAgIuLi850FxcXeV58fDycnZ115tepUwf29vZym+KEhIRAo9HIDw8PDwNXT0RERDVZjQ1AVWnu3LlISUmRH7du3TJ2SURERFSNamwAcnV1BQDcu3dPZ/q9e/fkea6urkhISNCZn5ubi6SkJLlNcczNzaFWq3UeREREpBw1NgA1bNgQrq6uOHDggDwtNTUVJ06cgI+PDwDAx8cHycnJOH36tNzm4MGD0Gq18Pb2rvaaiYiIqHaoY8yVp6Wl4dq1a/Lr69ev49y5c7C3t4enpyemT5+O999/H02bNkXDhg0xf/58uLu7y98Ua9GiBfz8/DB+/Hhs2LABOTk5mDJlCoYPH673N8CIiIhIeYwagE6dOoWePXvKr2fOnAkACAwMRFhYGGbPno309HRMmDABycnJ6NKlC/bu3QsLCwt5mS1btmDKlCno1asXVCoVhg4dijVr1lT7thAREVHtUWPuA2RMvA8QERFR7fNU3geIiIiIqKowABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIwABEREZHiMAARERGR4jAAERERkeIw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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAl0AAAHHCAYAAACFl+2TAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA1R0lEQVR4nO3de1xVVcL/8e85wDlcD4hykURUzNTE7IVmZBdLRrxkOdHda1ppYZNallZPajU509ikZWpNpTVPPs3UU5ZaGlrqzIiV2s1SRw0vpaipXEuu+/eHP/bDEVRAWFzm83691qt91l577bUPIN/2WmfjsCzLEgAAAOqVs6EHAAAA8J+A0AUAAGAAoQsAAMAAQhcAAIABhC4AAAADCF0AAAAGELoAAAAMIHQBAAAYQOgCAAAwgNAFoFn761//qs6dO8vPz09hYWHGz9+uXTuNHj3a+HkBND6ELqCJWLx4sRwOh118fX113nnnafTo0frpp58aeniN0vbt2zV69GjFx8frL3/5i15++eWzHvPVV19p+PDhio2NldvtVnh4uJKTk7Vo0SKVlpYaGDWA5sq3oQcAoGaeeOIJtW/fXidOnNDGjRu1ePFi/fOf/9TWrVvl7+/f0MNrVNauXauysjLNnTtXHTt2PGv7V155RePHj1dUVJRGjBih888/X3l5eVqzZo3Gjh2rgwcP6pFHHjEwcgDNEaELaGIGDhyonj17SpLuvPNOtWrVSn/84x/1wQcf6Oabb27g0TUuhw8flqRqTStu3LhR48ePV1JSkj788EOFhITY+yZOnKhNmzZp69at9TVUAP8BmF4EmrgrrrhCkrR79267rqioSI8//rgSExMVGhqqoKAgXXHFFfr000+9jt2zZ48cDodmz56tl19+WfHx8XK73erVq5e++OKLSud6++231bVrV/n7+6tbt2567733NHr0aLVr186rXVlZmebMmaMLL7xQ/v7+ioqK0rhx43T8+HGvdps2bVJKSopatWqlgIAAtW/fXmPGjKnWdc+fP18XXnih3G63YmJilJaWpuzsbHt/u3btNH36dElSRESEHA6HZsyYcdr+Zs6cKYfDoTfffNMrcJXr2bOn19qsgoICPfDAA/Y05AUXXKDZs2fLsqwzjnvGjBlyOByV6sunj/fs2eN1Dddee63Wrl2rnj17KiAgQAkJCVq7dq0k6d1331VCQoL8/f2VmJioL7/80qvP0aNHKzg4WD/99JOGDh2q4OBgRURE6MEHH6w0VfrWW28pMTFRISEh8ng8SkhI0Ny5c894LQBqhjtdQBNX/ku6RYsWdl1ubq5eeeUV3XbbbbrrrruUl5enV199VSkpKfr888/Vo0cPrz6WLFmivLw8jRs3Tg6HQ88884xuuOEG/fDDD/Lz85MkrVixQrfccosSEhI0a9YsHT9+XGPHjtV5551XaUzjxo3T4sWLdccdd+h3v/udMjMzNW/ePH355Zf617/+JT8/Px0+fFj9+/dXRESEpk6dqrCwMO3Zs0fvvvvuWa95xowZmjlzppKTk3XPPfdox44dWrBggb744gu7/zlz5uiNN97Qe++9pwULFig4OFjdu3evsr9ffvlFa9as0ZVXXqm2bdue9fyWZem6667Tp59+qrFjx6pHjx5atWqVpkyZop9++knPPffcWfuorl27dun222/XuHHjNHz4cM2ePVtDhgzRwoUL9cgjj+jee++VJM2aNUs333yzduzYIafz//5/urS0VCkpKerdu7dmz56t1atX69lnn1V8fLzuueceSVJ6erpuu+029evXT3/84x8lSdu2bdO//vUv3X///XV2LcB/PAtAk7Bo0SJLkrV69WrryJEj1v79+6133nnHioiIsNxut7V//367bUlJiVVYWOh1/PHjx62oqChrzJgxdl1mZqYlyWrZsqV17Ngxu/7999+3JFnLli2z6xISEqw2bdpYeXl5dt3atWstSVZcXJxd949//MOSZL355pte51+5cqVX/XvvvWdJsr744osavQ+HDx+2XC6X1b9/f6u0tNSunzdvniXJeu211+y66dOnW5KsI0eOnLHPr7/+2pJk3X///dUaw9KlSy1J1lNPPeVVf+ONN1oOh8PatWuXXRcXF2eNGjWq0phOVf71zczM9DpWkrVhwwa7btWqVZYkKyAgwNq7d69d/9JLL1mSrE8//dSuGzVqlCXJeuKJJ7zOdfHFF1uJiYn26/vvv9/yeDxWSUlJta4fQO0wvQg0McnJyYqIiFBsbKxuvPFGBQUF6YMPPlCbNm3sNj4+PnK5XJJOTvUdO3ZMJSUl6tmzp7Zs2VKpz1tuucXrTln5lOUPP/wgSTpw4IC+/fZbjRw5UsHBwXa7q666SgkJCV59vf322woNDdVvfvMb/fzzz3ZJTExUcHCwPcVZvs5q+fLlKi4urvb1r169WkVFRZo4caLXHZ277rpLHo9HK1asqHZf5XJzcyWpymnFqnz44Yfy8fHR7373O6/6Bx54QJZl6aOPPqrxGE6na9euSkpKsl/37t1bknTNNdd43ZUrry//mlU0fvx4r9dXXHGFV7uwsDAVFBQoPT29zsYNoDJCF9DEvPjii0pPT9c777yjQYMG6eeff5bb7a7U7vXXX1f37t3l7++vli1bKiIiQitWrFBOTk6ltqdOqZUHsPI1WHv37pWkKj8BeGrdzp07lZOTo8jISEVERHiV/Px8e3H7VVddpdTUVM2cOVOtWrXS9ddfr0WLFqmwsPCM118+lgsuuMCr3uVyqUOHDvb+mvB4PJKkvLy8arXfu3evYmJiKoW0Ll26eI2xLpz6tQkNDZUkxcbGVll/6ro5f39/RUREeNW1aNHCq929996rTp06aeDAgWrTpo3GjBmjlStX1tk1ADiJNV1AE3PJJZfYn14cOnSoLr/8ct1+++3asWOHfRfqv//7vzV69GgNHTpUU6ZMUWRkpHx8fDRr1iyvBfflfHx8qjyXdZZF4VUpKytTZGSk3nzzzSr3lwcAh8Ohd955Rxs3btSyZcu0atUqjRkzRs8++6w2btzodUetvnXs2FG+vr769ttv6/1cVS2il3TaZ4Cd7mtT3a/Z6dpVFBkZqa+++kqrVq3SRx99pI8++kiLFi3SyJEj9frrr5/1eADVw50uoAkrD1IHDhzQvHnz7Pp33nlHHTp00LvvvqsRI0YoJSVFycnJOnHiRK3OExcXJ+nkou5TnVoXHx+vo0ePqk+fPkpOTq5ULrroIq/2l156qX7/+99r06ZNevPNN/Xdd9/prbfeOutYduzY4VVfVFSkzMxMe39NBAYG6pprrtH69eu1f//+s7aPi4vTgQMHKt0Z2759u9cYq1J+F7HiJy2lur07Vhsul0tDhgzR/PnztXv3bo0bN05vvPFGlV9zALVD6AKauL59++qSSy7RnDlz7FBVfnej4l2Pzz77TBkZGbU6R0xMjLp166Y33nhD+fn5dv26desq3R26+eabVVpaqieffLJSPyUlJXbYOH78eKW7MuWfqjzTFGNycrJcLpeef/55r+NfffVV5eTkaPDgwTW9PEnS9OnTZVmWRowY4XWN5TZv3mzf9Rk0aJBKS0u9gq4kPffcc3I4HBo4cOBpzxMfHy9JWr9+vV1XUFDQoHeUjh496vXa6XTan/Q823QvgOpjehFoBqZMmaKbbrpJixcv1vjx43Xttdfq3Xff1W9/+1sNHjxYmZmZWrhwobp27VploKiOp59+Wtdff7369OmjO+64Q8ePH9e8efPUrVs3rz6vuuoqjRs3TrNmzdJXX32l/v37y8/PTzt37tTbb7+tuXPn6sYbb9Trr7+u+fPn67e//a3i4+OVl5env/zlL/J4PBo0aNBpxxEREaFp06Zp5syZGjBggK677jrt2LFD8+fPV69evTR8+PBaXd9ll12mF198Uffee686d+7s9UT6tWvX6oMPPtBTTz0lSRoyZIiuvvpqPfroo9qzZ48uuugiffzxx3r//fc1ceJEO1hVpX///mrbtq3Gjh2rKVOmyMfHR6+99poiIiK0b9++Wo39XN155506duyYrrnmGrVp00Z79+7VCy+8oB49etjr1ADUgQb85CSAGih/pEBVj1goLS214uPjrfj4eKukpMQqKyuznn76aSsuLs5yu93WxRdfbC1fvtwaNWqU1+Mdyh8Z8ac//alSn5Ks6dOne9W99dZbVufOnS23221169bN+uCDD6zU1FSrc+fOlY5/+eWXrcTERCsgIMAKCQmxEhISrIceesg6cOCAZVmWtWXLFuu2226z2rZta7ndbisyMtK69tprrU2bNlXr/Zg3b57VuXNny8/Pz4qKirLuuece6/jx415tqvvIiIo2b95s3X777VZMTIzl5+dntWjRwurXr5/1+uuvez2iIi8vz5o0aZLd7vzzz7f+9Kc/WWVlZV79nfrIiPJz9O7d23K5XFbbtm2tP//5z6d9ZMTgwYMrjVGSlZaW5lVX1ddy1KhRVlBQUKXjT31sxTvvvGP179/fioyMtMc0btw46+DBg9V6zwBUj8OyarFSFgD+vx49eigiIoLHDQDAWbCmC0C1FBcXq6SkxKtu7dq1+vrrr9W3b9+GGRQANCHc6QJQLXv27FFycrKGDx+umJgYbd++XQsXLlRoaKi2bt2qli1bNvQQAaBRYyE9gGpp0aKFEhMT9corr+jIkSMKCgrS4MGD9Yc//IHABQDVwJ0uAAAAA1jTBQAAYAChCwAAwADWdOnk34o7cOCAQkJCTvt30QAAQONiWZby8vIUExMjp7Px30cidEk6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zLFfOxwO5efna/r06Ro0aFBdjQ0AAKDZqNX04rPPPquUlBR17dpVJ06c0O23366dO3eqVatW+p//+Z+6HiMAAECTV6vQ1aZNG3399dd666239M033yg/P19jx47VsGHDvBbWAwAA4KRaP6fL19dXw4cP1zPPPKP58+frzjvvrHHgWr9+vYYMGaKYmBg5HA4tXbrUa//o0aPlcDi8yoABA7zaHDt2TMOGDZPH41FYWJjGjh3Ls8IAAECjU6s7XR988EGV9Q6HQ/7+/urYsaPat29/1n4KCgp00UUXacyYMbrhhhuqbDNgwAAtWrTIfu12u732Dxs2TAcPHlR6erqKi4t1xx136O6779aSJUtqcEUAAAD1q1aha+jQoXI4HLIsy6u+vM7hcOjyyy/X0qVL1aJFi9P2M3DgQA0cOPCM53K73YqOjq5y37Zt27Ry5Up98cUX6tmzpyTphRde0KBBgzR79mzFxMTU8MoAAADqR62mF9PT09WrVy+lp6crJydHOTk5Sk9PV+/evbV8+XKtX79eR48e1YMPPnjOA1y7dq0iIyN1wQUX6J577tHRo0ftfRkZGQoLC7MDlyQlJyfL6XTqs88+O22fhYWFys3N9SoAAAD1qVZ3uu6//369/PLLuuyyy+y6fv36yd/fX3fffbe+++47zZkzR2PGjDmnwQ0YMEA33HCD2rdvr927d+uRRx7RwIEDlZGRIR8fH2VlZSkyMtL7gnx9FR4erqysrNP2O2vWLM2cOfOcxgYAAFATtQpdu3fvlsfjqVTv8Xj0ww8/SJLOP/98/fzzz+c0uFtvvdXeTkhIUPfu3RUfH6+1a9eqX79+te532rRpmjx5sv06NzdXsbGx5zRWAACAM6nV9GJiYqKmTJmiI0eO2HVHjhzRQw89pF69ekmSdu7cWedBpkOHDmrVqpV27dolSYqOjtbhw4e92pSUlOjYsWOnXQcmnVwn5vF4vAoAAEB9qlXoevXVV5WZmak2bdqoY8eO6tixo9q0aaM9e/bolVdekSTl5+frscceq9PB/vjjjzp69Khat24tSUpKSlJ2drY2b95st/nkk09UVlam3r171+m5AQAAzkWtphcvuOACff/99/r444/173//2677zW9+I6fzZI4bOnToWfvJz8+371pJUmZmpr766iuFh4crPDxcM2fOVGpqqqKjo7V792499NBD6tixo1JSUiRJXbp00YABA3TXXXdp4cKFKi4u1oQJE3TrrbfyyUUAANCoOKxTn/tg0Nq1a3X11VdXqh81apQWLFigoUOH6ssvv1R2drZiYmLUv39/Pfnkk4qKirLbHjt2TBMmTNCyZcvkdDqVmpqq559/XsHBwdUeR25urkJDQ5WTk1PnU43tpq7Qnj8MrtM+AQBA/f7+rg+1utMlSWvWrNGaNWt0+PBhlZWVee177bXXqtVH3759Kz3rq6JVq1adtY/w8HAehAoAABq9WoWumTNn6oknnlDPnj3VunVrORyOuh4XAABAs1Kr0LVw4UItXrxYI0aMqOvxAAAANEu1+vRiUVGR14NRAQAAcGa1Cl133nkn66gAAABqoFbTiydOnNDLL7+s1atXq3v37vLz8/Pa/+c//7lOBgcAANBc1Cp0ffPNN+rRo4ckaevWrV77WFQPAABQWa1C16efflrX4wAAAGjWarWmCwAAADVT64ejbtq0SX//+9+1b98+FRUVee179913z3lgAAAAzUmt7nS99dZbuuyyy7Rt2za99957Ki4u1nfffadPPvlEoaGhdT1GAACAJq9Woevpp5/Wc889p2XLlsnlcmnu3Lnavn27br75ZrVt27auxwgAANDk1Sp07d69W4MHn/wjzi6XSwUFBXI4HJo0aZJefvnlOh0gAABAc1Cr0NWiRQvl5eVJks477zz7sRHZ2dn65Zdf6m50AAAAzUStFtJfeeWVSk9PV0JCgm666Sbdf//9+uSTT5Senq5rrrmmrscIAADQ5NUqdM2bN08nTpyQJD366KPy8/PThg0blJqaqgcffLBOBwgAANAc1Gp6MTw8XDExMSc7cDo1depU/f3vf1dMTIwuvvjiOh0gAABAc1Cj0FVYWKhp06apZ8+euuyyy7R06VJJ0qJFixQfH6+5c+dq0qRJ9TFOAACAJq1G04uPP/64XnrpJSUnJ2vDhg266aabdMcdd2jjxo169tlnddNNN8nHx6e+xgoAANBk1Sh0vf3223rjjTd03XXXaevWrerevbtKSkr09ddf84euAQAAzqBG04s//vijEhMTJUndunWT2+3WpEmTCFwAAABnUaPQVVpaKpfLZb/29fVVcHBwnQ8KAACguanR9KJlWRo9erTcbrck6cSJExo/fryCgoK82vEHrwEAALzVKHSNGjXK6/Xw4cPr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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAHHCAYAAABZbpmkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA/d0lEQVR4nO3dd3iUVf7+8XuSkEACSQiQDFlCr5EmkZKVDhKKCIKFHlgUS0Bp4hcbRdcIKKAugq4asCCKKygoJXSFSBNEQWmiAUmhSBomBHJ+f3hlfg4JLQxMeHi/rmsuM+eceZ7POTvZ3DxlxmaMMQIAALAoD3cXAAAAcC0RdgAAgKURdgAAgKURdgAAgKURdgAAgKURdgAAgKURdgAAgKURdgAAgKURdgAAgKURdoArULVqVQ0ePNjdZVjetGnTVL16dXl6eqpx48buLkeSNHHiRNlstiK9tmrVqrrzzjsvOW7dunWy2Wxat25dkfYDoHCEHdy05s6dK5vNpm3bthXa37ZtW9WvX/+q9/PVV19p4sSJV72dm8XKlSs1btw43X777YqLi9OLL75YYExubq7Kly+vli1bXnA7xhiFhYWpSZMm17LcYu3XX3+VzWZzPDw8PBQUFKQuXbooISHB3eUB142XuwsAbiR79+6Vh8eV/Rvhq6++0qxZswg8l2nNmjXy8PDQO++8I29v70LHlChRQvfee6/efPNN/fbbb6pSpUqBMRs2bNCRI0c0atQol9T1zDPP6P/+7/9csq3rrW/fvuratavOnTunffv26Y033lC7du20detWNWjQwN3lAdccR3aAK+Dj46MSJUq4u4wrkpWV5e4SrkhqaqpKlSp1waCTr3///jLG6KOPPiq0f/78+fLw8FCfPn2uqp789fPy8lLJkiWvalvu0qRJEw0YMEDR0dH697//rY8++kg5OTmaPXu2u0sDrgvCDnAFzr9mJzc3V5MmTVKtWrVUsmRJlStXTi1btlR8fLwkafDgwZo1a5YkOZ1OyJeVlaUxY8YoLCxMPj4+qlOnjl5++WUZY5z2++eff+qxxx5T+fLlVaZMGd111136/fffZbPZnI4Y5V9XsmfPHvXr109ly5Z1nOrZtWuXBg8erOrVq6tkyZKy2+3617/+pRMnTjjtK38b+/bt04ABAxQQEKAKFSro2WeflTFGhw8fVo8ePeTv7y+73a5XXnnlstbu7Nmzev7551WjRg35+PioatWqeuqpp5STk+MYY7PZFBcXp6ysLMdazZ07t9Dt3X777apatarmz59foC83N1effvqp2rVrp9DQ0Cuee2HrV9g1O3FxcWrfvr2Cg4Pl4+Oj8PDwiwaIlStXqnHjxipZsqTCw8P12WefXdbabd68WZ07d1ZAQIB8fX3Vpk0bbdy48bJeW5hWrVpJkg4ePFik+eRfg/TNN9+oWbNmKlmypKpXr6733nuvwNhdu3apTZs2KlWqlCpVqqQXXnhBcXFxstls+vXXX53GLlu2TK1atZKfn5/KlCmjbt26affu3U5jkpOTNWTIEFWqVEk+Pj6qWLGievToUWBbwN9xGgs3vbS0NB0/frxAe25u7iVfO3HiRMXGxuqBBx5Qs2bNlJ6erm3btum7777THXfcoYceekhHjx5VfHy83n//fafXGmN01113ae3atRo6dKgaN26sFStW6IknntDvv/+uGTNmOMYOHjxYn3zyiQYOHKgWLVpo/fr16tat2wXruvfee1WrVi29+OKLjuAUHx+vX375RUOGDJHdbtfu3bv11ltvaffu3fr2228L/CG///77Va9ePb300kv68ssv9cILLygoKEhvvvmm2rdvrylTpujDDz/U2LFj1bRpU7Vu3fqia/XAAw9o3rx5uueeezRmzBht3rxZsbGx+umnn7Ro0SJJ0vvvv6+33npLW7Zs0dtvvy1J+uc//1no9mw2m/r166cXX3xRu3fv1i233OLoW758uU6ePKn+/fsXae6FrV9hZs+erVtuuUV33XWXvLy8tGTJEj366KPKy8tTTEyM09j9+/fr/vvv18MPP6zo6GjFxcXp3nvv1fLly3XHHXdccB9r1qxRly5dFBERoQkTJsjDw8MRSr7++ms1a9bsIqteuPxgULZs2SLP58CBA7rnnns0dOhQRUdH691339XgwYMVERHh+N/i999/V7t27WSz2TR+/Hj5+fnp7bfflo+PT4Ga3n//fUVHRysqKkpTpkzR6dOnNXv2bLVs2VI7duxQ1apVJUm9e/fW7t27NWLECFWtWlWpqamKj49XYmKiYwxQgAFuUnFxcUbSRR+33HKL02uqVKlioqOjHc8bNWpkunXrdtH9xMTEmMJ+1RYvXmwkmRdeeMGp/Z577jE2m80cOHDAGGPM9u3bjSQzcuRIp3GDBw82ksyECRMcbRMmTDCSTN++fQvs7/Tp0wXaPvroIyPJbNiwocA2hg0b5mg7e/asqVSpkrHZbOall15ytP/xxx+mVKlSTmtSmJ07dxpJ5oEHHnBqHzt2rJFk1qxZ42iLjo42fn5+F91evt27dxtJZvz48U7tffr0MSVLljRpaWnGmCufe2Hrl9/3d4VtNyoqylSvXt2prUqVKkaS+d///udoS0tLMxUrVjS33nqro23t2rVGklm7dq0xxpi8vDxTq1YtExUVZfLy8pz2W61aNXPHHXcU2P/fHTp0yEgykyZNMseOHTPJycnm66+/Nk2bNjWSzMKFC69qPn9fu9TUVOPj42PGjBnjaBsxYoSx2Wxmx44djrYTJ06YoKAgI8kcOnTIGGNMRkaGCQwMNA8++KDTfpKTk01AQICj/Y8//jCSzLRp0y46b+B8nMbCTW/WrFmKj48v8GjYsOElXxsYGKjdu3dr//79V7zfr776Sp6ennrsscec2seMGSNjjJYtWybpr6MUkvToo486jRsxYsQFt/3www8XaCtVqpTj5+zsbB0/flwtWrSQJH333XcFxj/wwAOOnz09PXXbbbfJGKOhQ4c62gMDA1WnTh398ssvF6xF+muukjR69Gin9jFjxkiSvvzyy4u+/kLCw8N16623asGCBY62rKwsffHFF7rzzjvl7+8v6crnXtj6Febv280/QtimTRv98ssvSktLcxobGhqqu+++2/Hc399fgwYN0o4dO5ScnFzo9nfu3Kn9+/erX79+OnHihI4fP67jx48rKytLHTp00IYNG5SXl3fJOidMmKAKFSrIbrerVatW+umnn/TKK6/onnvuKfJ8wsPDHafDJKlChQoF3gvLly9XZGSk08cHBAUFOY645YuPj9epU6fUt29fxxyPHz8uT09PNW/eXGvXrnXU5+3trXXr1umPP/645LyBfJzGwk2vWbNmuu222wq0ly1bttDTW383efJk9ejRQ7Vr11b9+vXVuXNnDRw48LKC0m+//abQ0FCVKVPGqb1evXqO/vz/enh4qFq1ak7jatasecFtnz9Wkk6ePKlJkyZpwYIFSk1Ndeo7/w+ZJFWuXNnpeUBAgEqWLKny5csXaD//2pfz5c/h/JrtdrsCAwMdcy2K/v37a+zYsdq0aZP++c9/avHixTp9+rTTH9QrnXth61eYjRs3asKECUpISNDp06cLbDcgIMDxvGbNmgVOl9WuXVvSX6eV7HZ7ge3nh+jo6OgL1pCWllbgdNT5hg0bpnvvvVfZ2dlas2aNXnvtNZ07d+6q5nP++0P663fm7yHkt99+U2RkZIFx578P8ufZvn37QuvPD60+Pj6aMmWKxowZo5CQELVo0UJ33nmnBg0aVOj6AfkIO8BVaN26tQ4ePKjPP/9cK1eu1Ntvv60ZM2Zozpw5TkdGrre//ws933333adNmzbpiSeeUOPGjVW6dGnl5eWpc+fOhR4d8PT0vKw2SRe9ruXvivqhfBfTt29fjRs3TvPnz9c///lPzZ8/X2XLllXXrl0dY6507oWt3/kOHjyoDh06qG7dupo+fbrCwsLk7e2tr776SjNmzLisIy6Xkr+NadOmXfDDFUuXLn3J7dSqVUsdO3aUJN15553y9PTU//3f/6ldu3aOoH+l87na98Lf5W/7/fffLzS0eHn9/z9VI0eOVPfu3bV48WKtWLFCzz77rGJjY7VmzRrdeuutV7xv3BwIO8BVCgoK0pAhQzRkyBBlZmaqdevWmjhxoiPsXOgPfJUqVbRq1SplZGQ4Hd35+eefHf35/83Ly9OhQ4dUq1Ytx7gDBw5cdo1//PGHVq9erUmTJum5555ztBfl9FtR5M9h//79jiNXkpSSkqJTp04V+jk5lys0NFTt2rXTwoUL9eyzzyo+Pl6DBw923Lp+rea+ZMkS5eTk6IsvvnA6ypF/yuV8Bw4ckDHG6f2wb98+SbrghbU1atSQ9NeRjfyw4gpPP/20/vvf/+qZZ55xnCa90vlcjipVqhT6Pj2/LX+ewcHBlzXPGjVqaMyYMRozZoz279+vxo0b65VXXtEHH3xQ5FphbVyzA1yF80/flC5dWjVr1nS6ndrPz0+SdOrUKaex+R/y9p///MepfcaMGbLZbOrSpYskKSoqSpL0xhtvOI17/fXXL7vO/H+Fn/+v7pkzZ172Nq5G/lGW8/c3ffp0SbronWWXo3///kpNTdVDDz2k3Nxcp1NY12ruhW03LS1NcXFxhY4/evSo464zSUpPT9d7772nxo0bX/AUTEREhGrUqKGXX35ZmZmZBfqPHTtWpNoDAwP10EMPacWKFdq5c2eR5nM5oqKilJCQ4NiH9NcpxQ8//LDAOH9/f7344ouF3gWZP8/Tp08rOzvbqa9GjRoqU6aM0+8ccD6O7ABXITw8XG3btlVERISCgoK0bds2ffrppxo+fLhjTEREhCTpscceU1RUlDw9PdWnTx91795d7dq109NPP61ff/1VjRo10sqVK/X5559r5MiRjn/tRkREqHfv3po5c6ZOnDjhuPU8/6jA5Zwa8vf3V+vWrTV16lTl5ubqH//4h1auXKlDhw5dg1UpqFGjRoqOjtZbb72lU6dOqU2bNtqyZYvmzZunnj17ql27dle1/d69e+vRRx/V559/rrCwMKfb4K/V3Dt16iRvb291795dDz30kDIzM/Xf//5XwcHBSkpKKjC+du3aGjp0qLZu3aqQkBC9++67SklJuWiY8PDw0Ntvv60uXbrolltu0ZAhQ/SPf/xDv//+u9auXSt/f38tWbKkSPU//vjjmjlzpl566SUtWLDgiudzOcaNG6cPPvhAd9xxh0aMGOG49bxy5co6efKk473r7++v2bNna+DAgWrSpIn69OmjChUqKDExUV9++aVuv/12/ec//9G+ffvUoUMH3XfffQoPD5eXl5cWLVqklJSUq/7wSFic2+4DA9ws/9bzrVu3Ftrfpk2bS956/sILL5hmzZqZwMBAU6pUKVO3bl3z73//25w5c8Yx5uzZs2bEiBGmQoUKxmazOd2+nJGRYUaNGmVCQ0NNiRIlTK1atcy0adOcbjM2xpisrCwTExNjgoKCTOnSpU3Pnj3N3r17jSSnW8Hzb48+duxYgfkcOXLE3H333SYwMNAEBASYe++91xw9evSCt6+fv40L3RJe2DoVJjc310yaNMlUq1bNlChRwoSFhZnx48eb7Ozsy9rPpdx7771Gkhk3blyBvqud+9/7/u6LL74wDRs2NCVLljRVq1Y1U6ZMMe+++67TbdXG/PW+6datm1mxYoVp2LCh8fHxMXXr1i1w6/f5t57n27Fjh+nVq5cpV66c8fHxMVWqVDH33XefWb169UXXJP/W8wvdqj148GDj6enp+JiDK53P+dq0aWPatGlToPZWrVoZHx8fU6lSJRMbG2tee+01I8kkJycXmH9UVJQJCAgwJUuWNDVq1DCDBw8227ZtM8YYc/z4cRMTE2Pq1q1r/Pz8TEBAgGnevLn55JNPLroOgM2YIlxNBsDtdu7cqVtvvVUffPBBgVt5geJs5MiRevPNN5WZmXnBC50BV+KaHeAG8OeffxZomzlzpjw8PC75ycWAO53/3j1x4oTef/99tWzZkqCD64ZrdoAbwNSpU7V9+3a1a9dOXl5eWrZsmZYtW6Zhw4YpLCzM3eUBFxQZGam2bduqXr16SklJ0TvvvKP09HQ9++yz7i4NNxFOYwE3gPj4eE2aNEl79uxRZmamKleurIEDB+rpp592+gwSoLh56qmn9Omnn+rIkSOy2Wxq0qSJJkyY4NJb6YFLIewAAABL45odAABgaYQdAABgaZzs11/fy3L06FGVKVPmmnx3DwAAcD1jjDIyMhQaGioPjwsfvyHs6K+PceeOFgAAbkyHDx9WpUqVLthP2JEcX8J4+PBh+fv7u7kaAABwOdLT0xUWFub0ZcqFIexITt/PQtgBAODGcqlLUNx6gfLs2bPVsGFDR8iIjIzUsmXLHP3Z2dmKiYlRuXLlVLp0afXu3VspKSlO20hMTFS3bt3k6+ur4OBgPfHEEzp79uz1ngoAACim3Bp2KlWqpJdeeknbt2/Xtm3b1L59e/Xo0UO7d++WJI0aNUpLlizRwoULtX79eh09elS9evVyvP7cuXPq1q2bzpw5o02bNmnevHmaO3eunnvuOXdNCQAAFDPF7kMFg4KCNG3aNN1zzz2qUKGC5s+fr3vuuUeS9PPPP6tevXpKSEhQixYttGzZMt155506evSoQkJCJElz5szRk08+qWPHjsnb2/uy9pmenq6AgAClpaVxGgsAgBvE5f79Ljafs3Pu3DktWLBAWVlZioyM1Pbt25Wbm+v0keJ169ZV5cqVlZCQIElKSEhQgwYNHEFHkqKiopSenu44OlSYnJwcpaenOz0AAIA1uT3s/PDDDypdurR8fHz08MMPa9GiRQoPD1dycrK8vb0VGBjoND4kJETJycmSpOTkZKegk9+f33chsbGxCggIcDy47RwAAOtye9ipU6eOdu7cqc2bN+uRRx5RdHS09uzZc033OX78eKWlpTkehw8fvqb7AwAA7uP2W8+9vb1Vs2ZNSVJERIS2bt2qV199Vffff7/OnDmjU6dOOR3dSUlJkd1ulyTZ7XZt2bLFaXv5d2vljymMj4+PfHx8XDwTAABQHLn9yM758vLylJOTo4iICJUoUUKrV6929O3du1eJiYmKjIyUJEVGRuqHH35QamqqY0x8fLz8/f0VHh5+3WsHAADFj1uP7IwfP15dunRR5cqVlZGRofnz52vdunVasWKFAgICNHToUI0ePVpBQUHy9/fXiBEjFBkZqRYtWkiSOnXqpPDwcA0cOFBTp05VcnKynnnmGcXExHDkBgAASHJz2ElNTdWgQYOUlJSkgIAANWzYUCtWrNAdd9whSZoxY4Y8PDzUu3dv5eTkKCoqSm+88Ybj9Z6enlq6dKkeeeQRRUZGys/PT9HR0Zo8ebK7pgQAAIqZYvc5O+7A5+wAAHDjueE+ZwcAAOBaIOwAAABLI+wAAABLc/vn7FjdsWPHbrivo/D391eFChXcXQYAAC5B2LmGjh07pgFDHtDJjNPuLuWKBJXx1QdxbxN4AACWQNi5htLT03Uy47QqRPaWX1DIpV9QDGSdTNGxhP8pPT2dsAMAsATCznXgFxQi/+BK7i7jsh1zdwEAALgQFygDAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLI+wAAABLc2vYiY2NVdOmTVWmTBkFBwerZ8+e2rt3r9OYtm3bymazOT0efvhhpzGJiYnq1q2bfH19FRwcrCeeeEJnz569nlMBAADFlJc7d75+/XrFxMSoadOmOnv2rJ566il16tRJe/bskZ+fn2Pcgw8+qMmTJzue+/r6On4+d+6cunXrJrvdrk2bNikpKUmDBg1SiRIl9OKLL17X+QAAgOLHrWFn+fLlTs/nzp2r4OBgbd++Xa1bt3a0+/r6ym63F7qNlStXas+ePVq1apVCQkLUuHFjPf/883ryySc1ceJEeXt7X9M5AACA4q1YXbOTlpYmSQoKCnJq//DDD1W+fHnVr19f48eP1+nTpx19CQkJatCggUJCQhxtUVFRSk9P1+7duwvdT05OjtLT050eAADAmtx6ZOfv8vLyNHLkSN1+++2qX7++o71fv36qUqWKQkNDtWvXLj355JPau3evPvvsM0lScnKyU9CR5HienJxc6L5iY2M1adKkazQTAABQnBSbsBMTE6Mff/xR33zzjVP7sGHDHD83aNBAFStWVIcOHXTw4EHVqFGjSPsaP368Ro8e7Xienp6usLCwohUOAACKtWJxGmv48OFaunSp1q5dq0qVKl10bPPmzSVJBw4ckCTZ7XalpKQ4jcl/fqHrfHx8fOTv7+/0AAAA1uTWsGOM0fDhw7Vo0SKtWbNG1apVu+Rrdu7cKUmqWLGiJCkyMlI//PCDUlNTHWPi4+Pl7++v8PDwa1I3AAC4cbj1NFZMTIzmz5+vzz//XGXKlHFcYxMQEKBSpUrp4MGDmj9/vrp27apy5cpp165dGjVqlFq3bq2GDRtKkjp16qTw8HANHDhQU6dOVXJysp555hnFxMTIx8fHndMDAADFgFuP7MyePVtpaWlq27atKlas6Hh8/PHHkiRvb2+tWrVKnTp1Ut26dTVmzBj17t1bS5YscWzD09NTS5culaenpyIjIzVgwAANGjTI6XN5AADAzcutR3aMMRftDwsL0/r16y+5nSpVquirr75yVVkAAMBCisUFygAAANcKYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFgaYQcAAFiaW8NObGysmjZtqjJlyig4OFg9e/bU3r17ncZkZ2crJiZG5cqVU+nSpdW7d2+lpKQ4jUlMTFS3bt3k6+ur4OBgPfHEEzp79uz1nAoAACim3Bp21q9fr5iYGH377beKj49Xbm6uOnXqpKysLMeYUaNGacmSJVq4cKHWr1+vo0ePqlevXo7+c+fOqVu3bjpz5ow2bdqkefPmae7cuXruuefcMSUAAFDMeLlz58uXL3d6PnfuXAUHB2v79u1q3bq10tLS9M4772j+/Plq3769JCkuLk716tXTt99+qxYtWmjlypXas2ePVq1apZCQEDVu3FjPP/+8nnzySU2cOFHe3t7umBoAACgmitU1O2lpaZKkoKAgSdL27duVm5urjh07OsbUrVtXlStXVkJCgiQpISFBDRo0UEhIiGNMVFSU0tPTtXv37kL3k5OTo/T0dKcHAACwpmITdvLy8jRy5Ejdfvvtql+/viQpOTlZ3t7eCgwMdBobEhKi5ORkx5i/B538/vy+wsTGxiogIMDxCAsLc/FsAABAcVFswk5MTIx+/PFHLViw4Jrva/z48UpLS3M8Dh8+fM33CQAA3MOt1+zkGz58uJYuXaoNGzaoUqVKjna73a4zZ87o1KlTTkd3UlJSZLfbHWO2bNnitL38u7Xyx5zPx8dHPj4+Lp4FAAAojtx6ZMcYo+HDh2vRokVas2aNqlWr5tQfERGhEiVKaPXq1Y62vXv3KjExUZGRkZKkyMhI/fDDD0pNTXWMiY+Pl7+/v8LDw6/PRAAAQLHl1iM7MTExmj9/vj7//HOVKVPGcY1NQECASpUqpYCAAA0dOlSjR49WUFCQ/P39NWLECEVGRqpFixaSpE6dOik8PFwDBw7U1KlTlZycrGeeeUYxMTEcvQEAAO4NO7Nnz5YktW3b1qk9Li5OgwcPliTNmDFDHh4e6t27t3JychQVFaU33njDMdbT01NLly7VI488osjISPn5+Sk6OlqTJ0++XtMAAADFmFvDjjHmkmNKliypWbNmadasWRccU6VKFX311VeuLA0AAFhEsbkbCwAA4Fog7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsrUtj55ZdfXF0HAADANVGksFOzZk21a9dOH3zwgbKzs11dEwAAgMsUKex89913atiwoUaPHi273a6HHnpIW7ZscXVtAAAAV61IYadx48Z69dVXdfToUb377rtKSkpSy5YtVb9+fU2fPl3Hjh1zdZ0AAABFclUXKHt5ealXr15auHChpkyZogMHDmjs2LEKCwvToEGDlJSU5Ko6AQAAiuSqws62bdv06KOPqmLFipo+fbrGjh2rgwcPKj4+XkePHlWPHj1cVScAAECReBXlRdOnT1dcXJz27t2rrl276r333lPXrl3l4fFXdqpWrZrmzp2rqlWrurJWAACAK1aksDN79mz961//0uDBg1WxYsVCxwQHB+udd965quIAAACuVpHCzv79+y85xtvbW9HR0UXZPAAAgMsU6ZqduLg4LVy4sED7woULNW/evKsuCgAAwFWKFHZiY2NVvnz5Au3BwcF68cUXr7ooAAAAVylS2ElMTFS1atUKtFepUkWJiYlXXRQAAICrFCnsBAcHa9euXQXav//+e5UrV+6qiwIAAHCVIoWdvn376rHHHtPatWt17tw5nTt3TmvWrNHjjz+uPn36uLpGAACAIivS3VjPP/+8fv31V3Xo0EFeXn9tIi8vT4MGDeKaHQAAUKwUKex4e3vr448/1vPPP6/vv/9epUqVUoMGDVSlShVX1wcAAHBVihR28tWuXVu1a9d2VS0AAAAuV6Swc+7cOc2dO1erV69Wamqq8vLynPrXrFnjkuIAAACuVpHCzuOPP665c+eqW7duql+/vmw2m6vrAgAAcIkihZ0FCxbok08+UdeuXV1dDwAAgEsV6dZzb29v1axZ09W1AAAAuFyRws6YMWP06quvyhjj6noAAABcqkinsb755hutXbtWy5Yt0y233KISJUo49X/22WcuKQ4AAOBqFSnsBAYG6u6773Z1LQAAAC5XpLATFxfn6joAAACuiSJdsyNJZ8+e1apVq/Tmm28qIyNDknT06FFlZma6rDgAAICrVaQjO7/99ps6d+6sxMRE5eTk6I477lCZMmU0ZcoU5eTkaM6cOa6uEwAAoEiKdGTn8ccf12233aY//vhDpUqVcrTffffdWr16tcuKAwAAuFpFOrLz9ddfa9OmTfL29nZqr1q1qn7//XeXFAYAAOAKRTqyk5eXp3PnzhVoP3LkiMqUKXPVRQEAALhKkcJOp06dNHPmTMdzm82mzMxMTZgwga+QAAAAxUqRTmO98sorioqKUnh4uLKzs9WvXz/t379f5cuX10cffeTqGgEAAIqsSEd2KlWqpO+//15PPfWURo0apVtvvVUvvfSSduzYoeDg4MvezoYNG9S9e3eFhobKZrNp8eLFTv2DBw+WzWZzenTu3NlpzMmTJ9W/f3/5+/srMDBQQ4cO5fZ3AADgUKQjO5Lk5eWlAQMGXNXOs7Ky1KhRI/3rX/9Sr169Ch3TuXNnpw8x9PHxcerv37+/kpKSFB8fr9zcXA0ZMkTDhg3T/Pnzr6o2AABgDUUKO++9995F+wcNGnRZ2+nSpYu6dOly0TE+Pj6y2+2F9v30009avny5tm7dqttuu02S9Prrr6tr1656+eWXFRoaell1AAAA6ypS2Hn88cednufm5ur06dPy9vaWr6/vZYedy7Fu3ToFBwerbNmyat++vV544QWVK1dOkpSQkKDAwEBH0JGkjh07ysPDQ5s3b77g93fl5OQoJyfH8Tw9Pd1l9QIAgOKlSNfs/PHHH06PzMxM7d27Vy1btnTpBcqdO3fWe++9p9WrV2vKlClav369unTp4rjtPTk5ucA1Ql5eXgoKClJycvIFtxsbG6uAgADHIywszGU1AwCA4qXI1+ycr1atWnrppZc0YMAA/fzzzy7ZZp8+fRw/N2jQQA0bNlSNGjW0bt06dejQocjbHT9+vEaPHu14np6eTuABAMCiivxFoIXx8vLS0aNHXblJJ9WrV1f58uV14MABSZLdbldqaqrTmLNnz+rkyZMXvM5H+us6IH9/f6cHAACwpiId2fniiy+cnhtjlJSUpP/85z+6/fbbXVJYYY4cOaITJ06oYsWKkqTIyEidOnVK27dvV0REhCRpzZo1ysvLU/Pmza9ZHQAA4MZRpLDTs2dPp+c2m00VKlRQ+/bt9corr1z2djIzMx1HaSTp0KFD2rlzp4KCghQUFKRJkyapd+/estvtOnjwoMaNG6eaNWsqKipKklSvXj117txZDz74oObMmaPc3FwNHz5cffr04U4sAAAgqYhhJy8vzyU737Ztm9q1a+d4nn8dTXR0tGbPnq1du3Zp3rx5OnXqlEJDQ9WpUyc9//zzTp+18+GHH2r48OHq0KGDPDw81Lt3b7322msuqQ8AANz4XHaBclG0bdtWxpgL9q9YseKS2wgKCuIDBAEAwAUVKez8/U6mS5k+fXpRdgEAAOASRQo7O3bs0I4dO5Sbm6s6depIkvbt2ydPT081adLEMc5ms7mmSgAAgCIqUtjp3r27ypQpo3nz5qls2bKS/vqgwSFDhqhVq1YaM2aMS4sEAAAoqiJ9zs4rr7yi2NhYR9CRpLJly+qFF164oruxAAAArrUihZ309HQdO3asQPuxY8eUkZFx1UUBAAC4SpHCzt13360hQ4bos88+05EjR3TkyBH973//09ChQ9WrVy9X1wgAAFBkRbpmZ86cORo7dqz69eun3Nzcvzbk5aWhQ4dq2rRpLi0QAADgahQp7Pj6+uqNN97QtGnTdPDgQUlSjRo15Ofn59LiAAAArtZVfRFoUlKSkpKSVKtWLfn5+V30AwIBAADcoUhh58SJE+rQoYNq166trl27KikpSZI0dOhQbjsHAADFSpHCzqhRo1SiRAklJibK19fX0X7//fdr+fLlLisOAADgahXpmp2VK1dqxYoVqlSpklN7rVq19Ntvv7mkMAAAAFco0pGdrKwspyM6+U6ePOn0jeQAAADuVqSw06pVK7333nuO5zabTXl5eZo6daratWvnsuIAAACuVpFOY02dOlUdOnTQtm3bdObMGY0bN067d+/WyZMntXHjRlfXCAAAUGRFOrJTv3597du3Ty1btlSPHj2UlZWlXr16aceOHapRo4arawQAACiyKz6yk5ubq86dO2vOnDl6+umnr0VNAAAALnPFR3ZKlCihXbt2XYtaAAAAXK5Ip7EGDBigd955x9W1AAAAuFyRLlA+e/as3n33Xa1atUoREREFvhNr+vTpLikOAADgal1R2Pnll19UtWpV/fjjj2rSpIkkad++fU5jbDab66oDAAC4SlcUdmrVqqWkpCStXbtW0l9fD/Haa68pJCTkmhQHAABwta7omp3zv9V82bJlysrKcmlBAAAArlSkC5TznR9+AAAAipsrCjs2m63ANTlcowMAAIqzK7pmxxijwYMHO77sMzs7Ww8//HCBu7E+++wz11UIAABwFa4o7ERHRzs9HzBggEuLAQAAcLUrCjtxcXHXqg4AAIBr4qouUAYAACjuCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDS3Bp2NmzYoO7duys0NFQ2m02LFy926jfG6LnnnlPFihVVqlQpdezYUfv373cac/LkSfXv31/+/v4KDAzU0KFDlZmZeR1nAQAAijO3hp2srCw1atRIs2bNKrR/6tSpeu211zRnzhxt3rxZfn5+ioqKUnZ2tmNM//79tXv3bsXHx2vp0qXasGGDhg0bdr2mAAAAijkvd+68S5cu6tKlS6F9xhjNnDlTzzzzjHr06CFJeu+99xQSEqLFixerT58++umnn7R8+XJt3bpVt912myTp9ddfV9euXfXyyy8rNDT0us0FAAAUT8X2mp1Dhw4pOTlZHTt2dLQFBASoefPmSkhIkCQlJCQoMDDQEXQkqWPHjvLw8NDmzZuve80AAKD4ceuRnYtJTk6WJIWEhDi1h4SEOPqSk5MVHBzs1O/l5aWgoCDHmMLk5OQoJyfH8Tw9Pd1VZQMAgGKm2B7ZuZZiY2MVEBDgeISFhbm7JAAAcI0U27Bjt9slSSkpKU7tKSkpjj673a7U1FSn/rNnz+rkyZOOMYUZP3680tLSHI/Dhw+7uHoAAFBcFNuwU61aNdntdq1evdrRlp6ers2bNysyMlKSFBkZqVOnTmn79u2OMWvWrFFeXp6aN29+wW37+PjI39/f6QEAAKzJrdfsZGZm6sCBA47nhw4d0s6dOxUUFKTKlStr5MiReuGFF1SrVi1Vq1ZNzz77rEJDQ9WzZ09JUr169dS5c2c9+OCDmjNnjnJzczV8+HD16dOHO7EAAIAkN4edbdu2qV27do7no0ePliRFR0dr7ty5GjdunLKysjRs2DCdOnVKLVu21PLly1WyZEnHaz788EMNHz5cHTp0kIeHh3r37q3XXnvtus8FAAAUT24NO23btpUx5oL9NptNkydP1uTJky84JigoSPPnz78W5QEAAAsottfsAAAAuAJhBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWBphBwAAWFqxDjsTJ06UzWZzetStW9fRn52drZiYGJUrV06lS5dW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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6) checking the total class balance (whilst acknowledging the \"Info_cluster\" grouping structure) and visualing the distribution of class balance"
      ],
      "metadata": {
        "id": "uryaMSSEylng"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "IHQhVwlLw47z",
        "outputId": "86a6c514-a45c-4e63-e7a6-ed1ccdb05445"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Class Balance:\n",
            "Class\n",
            "-1    0.985002\n",
            " 1    0.014998\n",
            "Name: proportion, dtype: float64\n",
            "\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1kAAAIjCAYAAADxz9EgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB0LklEQVR4nO3deXxU9fX/8ffsM8lkIZCNGA0QKrsLClVUUFa1rdu3aqWtUHel7lr9tS7YWqvVal1atQuoda1brVog7oqI1j2ISBCEJiFBQvZMZru/P2imjNlmkptlMq/n48FDc9dz77n3zpy5934+FsMwDAEAAAAATGEd6AAAAAAAYCihyAIAAAAAE1FkAQAAAICJKLIAAAAAwEQUWQAAAABgIoosAAAAADARRRYAAAAAmIgiCwAAAABMRJEFAAAAACaiyAKQ1BobG3XmmWcqLy9PFotFF198cb/HcP3118tisfT7eocqi8Wi66+/fqDDSGpFRUVatGjRQIfRp5YvXy6LxaItW7YMdCgABiGKLAAJre2Lzr///e8ezf/rX/9ay5cv13nnnaeHHnpIP/rRj0yOcOA98sgjuuOOOwY6jCGhoqJC119/vT766KOBDgUAMIjZBzoAABhIr7zyir797W/ruuuuG+hQ+swjjzyi0tLSAblLNxBaWlpkt/fNx1tFRYWWLl2qoqIi7b///n2yDgBA4uNOFoCkVl1drczMzIEOI+GEw2H5fL6BDqNDbre7z4osAABiQZEFYMhZtGiRvF6vysvLdfzxx8vr9So7O1uXX365QqGQJOm1116TxWLR5s2b9cILL8hisUS9X1FdXa0zzjhDubm5crvd2m+//fTAAw/0KJ61a9fqmGOO0bBhw5SamqopU6bo97//fafTb9myRRaLRcuXL2837pvvGzU0NOjiiy9WUVGRXC6XcnJyNHfuXH3wwQeSpFmzZumFF17QV199FdnGoqKiyPytra267rrrVFxcLJfLpcLCQl155ZVqbW1tt94lS5bo4Ycf1sSJE+VyubRixYpOt+Ef//iHjj32WI0cOVIul0tjxozRL3/5y8j+39M999yj0aNHy+PxaNq0aXrzzTc1a9YszZo1KzKN3+/Xtddeq6lTpyojI0Opqak6/PDD9eqrr/Z6H7Xtp0mTJumzzz7TkUceqZSUFBUUFOiWW26JTPPaa6/p4IMPliQtXrw4sj87ylObtvftvvjiC/3whz9URkaGsrOzdc0118gwDG3btk3HHXec0tPTlZeXp9tuu63dMmLN0bJly3TUUUcpJydHLpdLEyZM0B//+Md2yysqKtJ3vvMdvfXWW5o2bZrcbrdGjx6tBx98sNPt2FM4HNbvf/97TZ48WW63W9nZ2VqwYEGXj+zW1NTo8ssv1+TJk+X1epWenq6jjz5aH3/8cbtp77rrLk2cOFEpKSkaNmyYDjroID3yyCOR8bHk85uefPJJWSwWvf766+3G3XfffbJYLCotLZUkffLJJ1q0aJFGjx4tt9utvLw8/eQnP9HOnTu73TedvQ/Y0TtqtbW1uvjii1VYWCiXy6Xi4mLdfPPNCofD3a4HwODHT30AhqRQKKT58+dr+vTpuvXWW/XSSy/ptttu05gxY3Teeedp/Pjxeuihh3TJJZdor7320mWXXSZJys7OVktLi2bNmqWysjItWbJEo0aN0t///nctWrRItbW1uuiii2KOo6SkRN/5zneUn5+viy66SHl5eVq/fr2ef/75uJbTmXPPPVdPPvmklixZogkTJmjnzp166623tH79eh144IH6+c9/rrq6Ov3nP//R7bffLknyer2Sdn9Z/t73vqe33npLZ599tsaPH69PP/1Ut99+u7744gs9++yzUet65ZVX9MQTT2jJkiUaMWJEVLH2TcuXL5fX69Wll14qr9erV155Rddee63q6+v129/+NjLdH//4Ry1ZskSHH364LrnkEm3ZskXHH3+8hg0bpr322isyXX19vf785z/rBz/4gc466yw1NDToL3/5i+bPn6933323y0f3uttHbXbt2qUFCxboxBNP1Mknn6wnn3xSP/vZzzR58mQdffTRGj9+vG644QZde+21Ovvss3X44YdLkg499NBu83TKKado/Pjx+s1vfqMXXnhBv/rVr5SVlaX77rtPRx11lG6++WY9/PDDuvzyy3XwwQfriCOOiDtHf/zjHzVx4kR973vfk91u1z//+U+df/75CofDuuCCC6LiKSsr0//93//pjDPO0Omnn66//vWvWrRokaZOnaqJEyd2uS1nnHGGli9frqOPPlpnnnmmgsGg3nzzTb3zzjs66KCDOpznyy+/1LPPPqvvf//7GjVqlKqqqnTfffdp5syZ+uyzzzRy5EhJ0p/+9CddeOGF+r//+z9ddNFF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r/PPP1/V1dU68MADdeONN0a+cHZWtI0ZM0Yff/yxZs+ebdrji9LuVvh27typp59+OtKAgyRt3rw5arq2/VhWVqYjjzwyMjwYDGrLli2aMmVKZNiTTz6p0aNH6+mnn46KNdb+zbrbR7Eycz/FItYc/fOf/1Rra6uee+65qLtUHbW+2Nt4Vq5cqZqamrjuZj355JM68sgj9Ze//CVqeG1tbbu7eampqTrllFN0yimnyO/368QTT9SNN96oq6++Wm63W1LP83nKKafogQce0Msvv6z169fLMIyoRwV37dqll19+WUuXLtW1114bGb5x48aYtnPYsGHtzlu/36/KysqoYWPGjFFjY2Nc1wUAiYXHBQHgG4455hht37496rGiYDCou+66S16vt13rZJ058MADNWrUKN1xxx3tvnh1dccgPT1dI0aMaPdexh/+8Ieov0OhULvHl3JycjRy5Mio5r1TU1M7fMzp5JNPVnl5uf70pz+1G9fS0qKmpqZOY+xK212SPbfR7/e3i/+ggw7S8OHD9ac//UnBYDAy/OGHH2732FpHy1y7dq3WrFnTZSyx7qNYpaamSmpfAPeVWHPU0f6pq6vTsmXLTI3npJNOkmEYkbtKe+rqmLbZbO3G//3vf1d5eXnUsG82k+50OjVhwgQZhqFAINDrfM6ZM0dZWVl6/PHH9fjjj2vatGlRj8F2tB8lxdza35gxY9qdt/fff3+7O1knn3yy1qxZo5UrV7ZbRm1tbdT5ACAxcScLAL7h7LPP1n333adFixbp/fffV1FRkZ588kmtXr1ad9xxh9LS0mJajtVq1R//+Ed997vf1f7776/FixcrPz9fn3/+udatW9fhF6w2Z555pn7zm9/ozDPP1EEHHaQ33nhDX3zxRdQ0DQ0N2muvvfR///d/2m+//eT1evXSSy/pvffei+pvaerUqXr88cd16aWX6uCDD5bX69V3v/td/ehHP9ITTzyhc889V6+++qpmzJihUCikzz//XE888YRWrlzZaZPcXTn00EM1bNgwnX766brwwgtlsVj00EMPtfvi6nQ6df311+unP/2pjjrqKJ188snasmWLli9frjFjxkTdufnOd76jp59+WieccIKOPfZYbd68Wffee68mTJigxsbGTmOJdR/FasyYMcrMzNS9996rtLQ0paamavr06XG9rxaPWHM0b948OZ1O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1boqjR7hjfnRQSSfuIusSy+9VIsWLdItt9yitLT/VfDHHHOMTjvtNFOD21NWVpYeeeSRTscXFRXJMIwul9HdeAAAACS38toWbdrRqPwMd6TAamOxWJSf4VZZdaPKa1tUmNW7lqcxdFnjneG9997TOeec0254QUFBl82pAwAAAINdkz8oXzCkFGfH9yI8TptagyE1+YP9HBkSSdxFlsvl6rDpwi+++CKmRiwAAACAwSrVaZfbblNzJ0VUiz8kl92m1E6KMEDqQZH1ve99TzfccEOkt2OLxaKtW7fqZz/7mU466STTAwQAAAD6S0GmR2Oyvaqs87V71cQwDFXW+VSc41VBpmeAIkQiiLvIuu2229TY2KicnBy1tLRo5syZKi4uVlpamm688ca+iBEAAADoF1arRfMn5Sor1amN1Y1q8AUUDIfV4AtoY3WjslKdmjcxl0Yv0KW473NmZGSopKREb731lj755BM1NjbqwAMP1Jw5c/oiPgAAAKBfFeekafGMokg/WVX1PrnsNk0uyNC8ifSThe71+GHSww47TIcddpiZsQAAAACDQnFOmkbP8qq8tkVN/qBSnXYVZHq4g4WYxF1k3XDDDV2Ov/baa3scDAAAADBYWK0WmmlHj8RdZD3zzDNRfwcCAW3evFl2u11jxoyhyAIAAACQ1OIusj788MN2w+rr67Vo0SKdcMIJpgQFAAAAAIkq7tYFO5Kenq6lS5fqmmuuMWNxAAAAAJCwTCmyJKmurk51dXVmLQ4AAAAAElLcjwveeeedUX8bhqHKyko99NBDOvroo00LDAAAAAASUdxF1u233x71t9VqVXZ2tk4//XRdffXVpgUGAAAAAIko7iJr8+bNfREHAAAAAAwJpr2TBQAAAACI8U7WiSeeGPMCn3766R4HAwAAAACJLqYiKyMjo6/jAAAAAIAhIaYia9myZX0dBwAAAAAMCbyTBQAAAAAmirt1QUl68skn9cQTT2jr1q3y+/1R4z744ANTAgMAAACARBT3naw777xTixcvVm5urj788ENNmzZNw4cP15dffklnxAAAAACSXtxF1h/+8Afdf//9uuuuu+R0OnXllVeqpKREF154oerq6voiRgAAAABIGHEXWVu3btWhhx4qSfJ4PGpoaJAk/ehHP9Kjjz5qbnQAAAAAkGDiLrLy8vJUU1MjSdp77731zjvvSJI2b94swzDMjQ4AAKCfhcOGttU06/Pt9dpW06xwmO83AOITd8MXRx11lJ577jkdcMABWrx4sS655BI9+eST+ve//x1Xp8UAAACDTVl1g1aWVmnTjkb5giG57TaNyfZq/qRcFeekDXR4ABJEzEXW888/r2OOOUb333+/wuGwJOmCCy7Q8OHD9fbbb+t73/uezjnnnD4LFAAAoC+VVTdo2eotqmnyKz/DrRSnR83+oEor6lRR16LFM4ootADEJOYi6/jjj1dubq4WLVqkn/zkJxozZowk6dRTT9Wpp57aZwECAAD0tXDY0MrSKtU0+TU2xyuLxSJJSnM75HXZtbG6UavWVWn0CK+sVssARwtgsIv5nazNmzfrnHPO0WOPPaZvfetbmjlzph566CG1tLT0ZXwAAAB9rry2RZt2NCo/wx0psNpYLBblZ7hVVt2o8lq+9wDoXsxFVmFhoa699lpt2rRJL730koqKinTeeecpPz9f5557rt57772+jBMAAKDPNPmD8gVDSnF2/JCPx2lTazCkJn+wnyMDkIjibl1Qko488kg98MADqqys1G9/+1t9+umn+va3v6399tvP7PgAAAD6XKrTLrfdpuZOiqgWf0guu02pnRRhALCnHhVZbdLS0jR79mwdeeSRyszM1GeffWZWXAAAAP2mINOjMdleVdb52nVJYxiGKut8Ks7xqiDTM0ARAkgkPSqyWlpa9OCDD2rWrFkaO3asHnvsMV166aXasmWLyeEBAAD0PavVovmTcpWV6tTG6kY1+AIKhsNq8AW0sbpRWalOzZuYS6MXAGIS1z3vd955R3/961/1xBNPyO/368QTT9RLL72kI488sq/iAwAA6BfFOWlaPKMo0k9WVb1PLrtNkwsyNG8i/WQBiF3MRdaECRO0YcMGHXDAAbrpppt02mmnKSMjoy9jAwD0QDhsqLy2RU3+oFKddhVkevj1HYhRcU6aRs/ycg4B6JWYi6w5c+bo0UcfpXELABjEyqobIr/C+4Ihue02jcn2av4kfoUHYmW1WlSYlTLQYQBIYDEXWXfeeWdfxgEA6KWy6gYtW71FNU1+5We4leL0qNkfVGlFnSrqWrR4RhGFFgAA/aBXrQsCAAaHcNjQytIq1TT5NTbHqzS3QzarRWluh8bmeFXT5NeqdVUKh43uFwYAAHqFIgsAhoDy2hZt2tGo/Ay3LJbod0csFovyM9wqq25UeW3LAEUIAEDyoMgCgCGgyR+ULxhSSicdpXqcNrUGQ2rqpKNVAABgHlOKrNraWjMWAwDooVSnXW67Tc2dFFEt/pBcdptSOynCAACAeeIusm6++WY9/vjjkb9PPvlkDR8+XAUFBfr4449NDQ4AEJuCTI/GZHtVWeeTYUS/d2UYhirrfCrO8aog0zNAEQIAkDziLrLuvfdeFRYWSpJKSkpUUlKif/3rXzr66KN1xRVXmB4gAKB7VqtF8yflKivVqY3VjWrwBRQMh9XgC2hjdaOyUp2aNzGXvn4AAOgHcT83sn379kiR9fzzz+vkk0/WvHnzVFRUpOnTp5seIAAgNsU5aVo8oyjST1ZVvU8uu02TCzI0byL9ZAEA0F/iLrKGDRumbdu2qbCwUCtWrNCvfvUrSbsfRwmFQqYHCACIXXFOmkbP8qq8tkVN/qBSnXYVZHq4gwUAQD+Ku8g68cQTddppp2ns2LHauXOnjj76aEnShx9+qOLiYtMDBADEx2q1qDArZaDDAAAgacVdZN1+++0qKirStm3bdMstt8jr9UqSKisrdf7555seIAAAAAAkkriLLIfDocsvv7zd8EsuucSUgAAAAAAgkcXduuADDzygF154IfL3lVdeqczMTB166KH66quvTA0OAAAAABJN3EXWr3/9a3k8u/tZWbNmje655x7dcsstGjFiBHezAAAAACS9uB8X3LZtW6SBi2effVYnnXSSzj77bM2YMUOzZs0yOz4AAAAASChx38nyer3auXOnJGnVqlWaO3euJMntdqulpcXc6AAAAAAgwcR9J2vu3Lk688wzdcABB+iLL77QMcccI0lat26dioqKzI4PAAAAABJK3Hey7rnnHh1yyCHasWOHnnrqKQ0fPlyS9P777+sHP/iB6QECAAAAQCKJ+05WZmam7r777nbDly5dakpAAAAAAJDI4i6y2jQ3N2vr1q3y+/1Rw6dMmdLroAAAAAAgUcVdZO3YsUOLFi3SihUrOhwfCoV6HRQAAAAAJKq438m6+OKLVVdXp7Vr18rj8WjFihV64IEHNHbsWD333HN9ESMAAAAAJIy472S98sor+sc//qGDDjpIVqtV++yzj+bOnav09HTddNNNOvbYY/siTgAAAABICHHfyWpqalJOTo4kadiwYdqxY4ckafLkyfrggw/MjQ4AAAAAEkzcRda+++6rDRs2SJL2228/3XfffSovL9e9996r/Px80wMEAAAAgEQS9+OCF110kSorKyVJ1113nRYsWKCHH35YTqdTy5cvNzs+AAAAAEgocRdZP/zhDyP/P3XqVH311Vf6/PPPtffee2vEiBGmBgcAAAAAiabH/WS1SUlJ0YEHHmhGLAAAAACQ8GIqsi699NKYF/i73/2ux8EAAAAAQKKLqcj68MMPY1qYxWLpVTAAAAAAkOhiKrJeffXVvo4DAAAAAIaEmJtwD4VC+uSTT9TS0tJuXEtLiz755BOFw2FTgwMAAAAw+ITDhrbVNOvz7fXaVtOscNgY6JAGlZgbvnjooYd09913a+3ate3GORwO/eQnP9HFF18c1fogAAAAgKGlrLpBK0urtGlHo3zBkNx2m8ZkezV/Uq6Kc9IGOrxBIeY7WX/5y190+eWXy2aztRtnt9t15ZVX6v777zc1OAAAAACDR1l1g5at3qLSijplpjg0eoRXmSkOlVbUadnqLSqrbhjoEAeFmIusDRs26Nvf/nan4w8++GCtX7/elKAAAAAADC7hsKGVpVWqafJrbI5XaW6HbFaL0twOjc3xqqbJr1Xrqnh0UHEUWU1NTaqvr+90fENDg5qbm00JCgAAAMDgUl7bok07GpWf4W7XqrjFYlF+hltl1Y0qr23fhkOyibnIGjt2rN5+++1Ox7/11lsaO3asKUEBAAAAGFya/EH5giGlODtu1sHjtKk1GFKTP9jPkQ0+MRdZp512mn7xi1/ok08+aTfu448/1rXXXqvTTjvN1OAAAAAADA6pTrvcdpuaOymiWvwhuew2pXZShCWTmPfAJZdcon/961+aOnWq5syZo3HjxkmSPv/8c7300kuaMWOGLrnkkj4LFAAAAMDAKcj0aEy2V6UVdfK67FGPDBqGoco6nyYXZKgg0zOAUQ4OMRdZDodDq1at0u23365HHnlEb7zxhgzD0Le+9S3deOONuvjii+VwOPoyVgAAAAADxGq1aP6kXFXUtWhj9e53szxOm1r8IVXW+ZSV6tS8ibmyWi3dL2yIi+tensPh0JVXXqkrr7yyr+IBAAAAMEgV56Rp8YyiSD9ZVfU+uew2TS7I0LyJ9JPVhgcmAQAAAMSsOCdNo2d5VV7boiZ/UKlOuwoyPdzB2gNFFgAAAIC4WK0WFWalDHQYg1bMrQsCAAAAALpHkQUAAAAAJkqYIqumpkYLFy5Uenq6MjMzdcYZZ6ixsbHb+dasWaOjjjpKqampSk9P1xFHHKGWFnqhBgAAANA34n4nKxQKafny5Xr55ZdVXV2tcDgcNf6VV14xLbg9LVy4UJWVlSopKVEgENDixYt19tln65FHHul0njVr1mjBggW6+uqrddddd8lut+vjjz+W1ZowtSUAAACABBN3kXXRRRdp+fLlOvbYYzVp0qSoTsj6yvr167VixQq99957OuiggyRJd911l4455hjdeuutGjlyZIfzXXLJJbrwwgt11VVXRYbtu+++fR4vAAAAgOQVd5H12GOP6YknntAxxxzTF/F0aM2aNcrMzIwUWJI0Z84cWa1WrV27VieccEK7eaqrq7V27VotXLhQhx56qDZt2qRx48bpxhtv1GGHHdbpulpbW9Xa2hr5u76+XpIUCAQUCAR6FH/bfD2dH4mN/Cc38p+8yH1yI//Ji9wPbbHmNe4iy+l0qri4OO6AemP79u3KycmJGma325WVlaXt27d3OM+XX34pSbr++ut16623av/999eDDz6o2bNnq7S0VGPHju1wvptuuklLly5tN3zVqlVKSeldM5UlJSW9mh+JjfwnN/KfvMh9ciP/yYvcD03Nzc0xTRd3kXXZZZfp97//ve6+++5ePyp41VVX6eabb+5ymvXr1/do2W3vip1zzjlavHixJOmAAw7Qyy+/rL/+9a+66aabOpzv6quv1qWXXhr5u76+XoWFhZo3b57S09N7FEsgEFBJSYnmzp0rh8PRo2UgcZH/5Eb+kxe5T27kP3mR+6Gt7Sm37sRdZL311lt69dVX9a9//UsTJ05sd/A8/fTTMS/rsssu06JFi7qcZvTo0crLy1N1dXXU8GAwqJqaGuXl5XU4X35+viRpwoQJUcPHjx+vrVu3dro+l8sll8vVbrjD4ej1iWLGMpC4yH9yI//Ji9wnN/KfvMj90BRrTuMusjIzMzt8B6onsrOzlZ2d3e10hxxyiGpra/X+++9r6tSpkna3YhgOhzV9+vQO5ykqKtLIkSO1YcOGqOFffPGFjj766N4HDwAAAAAdiLvIWrZsWV/E0aXx48drwYIFOuuss3TvvfcqEAhoyZIlOvXUUyMtC5aXl2v27Nl68MEHNW3aNFksFl1xxRW67rrrtN9++2n//ffXAw88oM8//1xP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OuiggyLTzJkzR1arVWvXru33mGG+1157TTk5Odp333113nnnaefOnZFx5H/oqKurkyRlZWVJiu16v2bNGk2ePFm5ubmRaebPn6/6+nqtW7euH6NHb3wz920efvhhjRgxQpMmTdLVV1+t5ubmyDhyn1zsAx3AUPb1118rFApFnUySlJubq88//3yAokJfmD59upYvX659991XlZWVWrp0qQ4//HCVlpZq+/btcjqdyszMjJonNzdX27dvH5iA0WfactrRed82bvv27crJyYkab7fblZWVxTExBCxYsEAnnniiRo0apU2bNun//b//p6OPPlpr1qyRzWYj/0NEOBzWxRdfrBkzZmjSpEmSFNP1fvv27R1eH9rGYfDrKPeSdNppp2mfffbRyJEj9cknn+hnP/uZNmzYoKeffloSuU82FFmACY4++ujI/0+ZMkXTp0/XPvvsoyeeeEIej2cAIwPQ30499dTI/0+ePFlTpkzRmDFj9Nprr2n27NkDGBnMdMEFF6i0tDTq/Vskh85yv+d7lZMnT1Z+fr5mz56tTZs2acyYMf0dJgYYjwv2oREjRshms7VrVaiqqkp5eXkDFBX6Q2Zmpr71rW+prKxMeXl58vv9qq2tjZqG42BoastpV+d9Xl5eu8ZvgsGgampqOCaGoNGjR2vEiBEqKyuTRP6HgiVLluj555/Xq6++qr322isyPJbrfV5eXofXh7ZxGNw6y31Hpk+fLklR5z65Tx4UWX3I6XRq6tSpevnllyPDwuGwXn75ZR1yyCEDGBn6WmNjozZt2qT8/HxNnTpVDocj6jjYsGGDtm7dynEwBI0aNUp5eXlR+a6vr9fatWsj+T7kkENUW1ur999/PzLNK6+8onA4HPlQxtDxn//8Rzt37lR+fr4k8p/IDMPQkiVL9Mwzz+iVV17RqFGjosbHcr0/5JBD9Omnn0YV2iUlJUpPT9eECRP6Z0MQt+5y35GPPvpIkqLOfXKfRAa65Y2h7rHHHjNcLpexfPly47PPPjPOPvtsIzMzM6plGSS+yy67zHjttdeMzZs3G6tXrzbmzJljjBgxwqiurjYMwzDOPfdcY++99zZeeeUV49///rdxyCGHGIcccsgAR42eamhoMD788EPjww8/NCQZv/vd74wPP/zQ+OqrrwzDMIzf/OY3RmZmpvGPf/zD+OSTT4zjjjvOGDVqlNHS0hJZxoIFC4wDDjjAWLt2rfHWW28ZY8eONX7wgx8M1CYhDl3lv6Ghwbj88suNNWvWGJs3bzZeeukl48ADDzTGjh1r+Hy+yDLIf2I677zzjIyMDOO1114zKisrI/+am5sj03R3vQ8Gg8akSZOMefPmGR999JGxYsUKIzs727j66qsHYpMQo+5yX1ZWZtxwww3Gv//9b2Pz5s3GP/7xD2P06NHGEUccEVkGuU8uFFn94K677jL23ntvw+l0GtOmTTPeeeedgQ4JJjvllFOM/Px8w+l0GgUFBcYpp5xilJWVRca3tLQY559/vjFs2DAjJSXFOOGEE4zKysoBjBi98eqrrxqS2v07/fTTDcPY3Yz7NddcY+Tm5houl8uYPXu2sWHDhqhl7Ny50/jBD35geL1eIz093Vi8eLHR0NAwAFuDeHWV/+bmZmPevHlGdna24XA4jH322cc466yz2v2wRv4TU0d5l2QsW7YsMk0s1/stW7YYRx99tOHxeIwRI0YYl112mREIBPp5axCP7nK/detW44gjjjCysrIMl8tlFBcXG1dccYVRV1cXtRxynzwshmEY/XffDAAAAACGNt7JAgAAAAATUWQBAAAAgIkosgAAAADARBRZAAAAAGAiiiwAAAAAMBFFFgAAAACYiCILAAAAAExEkQUAAAAAJqLIAgAktO3bt2vu3LlKTU1VZmZmn6+vqKhId9xxR5+vBwCQuCiyAACDyqJFi3T88cfHPP3tt9+uyspKffTRR/riiy/6LrA+sGXLFlksFn300UcDHQoAwET2gQ4AAIDe2LRpk6ZOnaqxY8cOdCgDKhAIyOFwDHQYAABxJwsAMIjNmjVLF154oa688kplZWUpLy9P119/fWR8UVGRnnrqKT344IOyWCxatGiRJGnr1q067rjj5PV6lZ6erpNPPllVVVUxr/ef//ynDj74YLndbo0YMUInnHBCh9N1dCeqtrZWFotFr732miRp165dWrhwobKzs+XxeDR27FgtW7ZMkjRq1ChJ0gEHHCCLxaJZs2ZFlvPnP/9Z48ePl9vt1rhx4/SHP/yh3Xoff/xxzZw5U263Ww8//HDM2wcA6FvcyQIADGoPPPCALr30Uq1du1Zr1qzRokWLNGPGDM2dO1fvvfeefvzjHys9PV2///3v5fF4FA6HIwXW66+/rmAwqAsuuECnnHJKpPDpygsvvKATTjhBP//5z/Xggw/K7/frxRdf7HH811xzjT777DP961//0ogRI1RWVqaWlhZJ0rvvvqtp06bppZde0sSJE+V0OiVJDz/8sK699lrdfffdOuCAA/Thhx/qrLPOUmpqqk4//fTIsq+66irddtttOuCAA+R2u3scIwDAXBRZAIBBbcqUKbruuuskSWPHjtXdd9+tl19+WXPnzlV2drZcLpc8Ho/y8vIkSSUlJfr000+1efNmFRYWSpIefPBBTZw4Ue+9954OPvjgLtd344036tRTT9XSpUsjw/bbb78ex79161YdcMABOuiggyTtvvvWJjs7W5I0fPjwSPySdN111+m2227TiSeeKGn3Ha/PPvtM9913X1SRdfHFF0emAQAMHjwuCAAY1KZMmRL1d35+vqqrqzudfv369SosLIwUWJI0YcIEZWZmav369d2u76OPPtLs2bN7HvA3nHfeeXrssce0//7768orr9Tbb7/d5fRNTU3atGmTzjjjDHm93si/X/3qV9q0aVPUtG2FGwBgcOFOFgBgUPtmYw4Wi0XhcLjP1ufxeGKe1mrd/VulYRiRYYFAIGqao48+Wl999ZVefPFFlZSUaPbs2brgggt06623drjMxsZGSdKf/vQnTZ8+PWqczWaL+js1NTXmWAEA/Yc7WQCAIWX8+PHatm2btm3bFhn22Wefqba2VhMmTOh2/ilTpujll1+OaV1tj/tVVlZGhnXUHHt2drZOP/10/e1vf9Mdd9yh+++/X5Ii72CFQqHItLm5uRo5cqS+/PJLFRcXR/1raygDADC4cScLADCkzJkzR5MnT9bChQt1xx13KBgM6vzzz9fMmTNjerzuuuuu0+zZszVmzBideuqpCgaDevHFF/Wzn/2s3bQej0ff/va39Zvf/EajRo1SdXW1fvGLX0RNc+2112rq1KmaOHGiWltb9fzzz2v8+PGSpJycHHk8Hq1YsUJ77bWX3G63MjIytHTpUl144YXKyMjQggUL1Nraqn//+9/atWuXLr30UnN2FACgz3AnCwAwpFgsFv3jH//QsGHDdMQRR2jOnDkaPXq0Hn/88ZjmnzVrlv7+97/rueee0/7776+jjjpK7777bqfT//Wvf1UwGNTUqVN18cUX61e/+lXUeKfTqauvvlpTpkzREUccIZvNpscee0ySZLfbdeedd+q+++7TyJEjddxxx0mSzjzzTP35z3/WsmXLNHnyZM2cOVPLly/nThYAJAiLseeD5AAAAACAXuFOFgAAAACYiCILAJBUJk6cGNU0+p7/Hn744YEODwAwBPC4IAAgqXz11Vftmllvk5ubq7S0tH6OCAAw1FBkAQAAAICJeFwQAAAAAExEkQUAAAAAJqLIAgAAAAATUWQBAAAAgIkosgAAAADARBRZAAAAAGAiiiwAAAAAMNH/B+qRqajmhDiMAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAksAAAGxCAYAAAByXPLgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABBjklEQVR4nO3de3wU5d3///duDptwSALmLFGCoBA5JA0Qo1b5mpQEsAX0vgsWb4QfQkXRW4Mi2AKiVqwHSq1U1IpghUqx4glNxVD0tsaAwRSQg4JoQLIJp2RJgJx2fn8ga5YkkyUs2Sy+no/HPmBnrrn2M9fOTt6ZmZ1YDMMwBAAAgCZZfV0AAABAe0ZYAgAAMEFYAgAAMEFYAgAAMEFYAgAAMEFYAgAAMEFYAgAAMEFYAgAAMEFY8gLDMORwOMT9PQEAOP8Qlrzg6NGjCg8P19GjR31dCgAA8DLCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAnCEgAAgAm/CksfffSRfv7znys+Pl4Wi0VvvPFGi8usX79eP/nJT2Sz2dSzZ08tXbq0UZtFixape/fuCgkJUVpamjZs2OD94s+BvYcr9f42u/YerjRt988t+3XX3zbpn1v2u6btKnPotcK92lXmONdl+g1vjUmZ47gK9hxSmeO4lyo7906vueJYjb4sPaqKYzUe99Fwe1xdWKwJSwq0urC4xeVO1NbrYGW1VhcW69cvb9Q7RftM2z+7boeGLviXnl23w+PazqX29llqbr/Qmjo//rJMc9/cqo+/LGvUz8dflnm0/3mnaJ9H72tLn5v2Ns7Naeqz09Ln6Q+5W3Xt43n6Q+5Wrdtm14zX/qN12+yN2hUVH9Yz675SUfHhM67LF/ulU6/58Zdleunfe7Rtf3mbvba3WQzDMHxdhKfee+89/fvf/1ZqaqpuuOEGrV69WqNGjWq2/Z49e9S3b1/ddtttuvXWW5WXl6e7775ba9asUVZWliRp5cqVGj9+vBYvXqy0tDQtXLhQq1at0s6dOxUdHe1RXQ6HQ+Hh4aqoqFBYWJg3VtXUe5tLdN9rRaqscbqmdbYF6KkxyRqaFOuadvsrn+ndraUt9hccYNGjN/TTf6UmnJN627uVBcX67ZtbVPvDcLZqTPJ3HdT0VUXaX1HtmnZhRIgWjElWWuIF3izZa5qqOSjAIsNpSBaLrFaLUhIi9PCovro0pnOTfTS1PZ5uyKWRWvr/pblNO3C0Wq98+o2e/2iXjtc2XiYrKVrPjR/kep755DrtOth4R39pdAe9n/P/WlpVr/PWduMtze0XRqdcqL9tKD6jOn/z+mYt37DX49duav8zaWmB8nYcbNT29Pe1pc9Nexvn5uwocWjOm1tVtK9CTqchq9Wiy2I6yTAMfVlW5ZrW8PP008c+0N7yatN+fzmwm+LDQrRw3a5G8+4deqmmXdfLdHlf7Jeaes1TrBZp9vVJmnhV4jl57XPFr8JSQxaLpcWwdP/992vNmjXaunWra9rYsWNVXl6u3NxcSVJaWpoGDRqkZ555RpLkdDqVkJCgO++8UzNnzvSolrYMS+9tLtHUFZuanf/8+FQNTYr1OCg19OR/929XO5+2sLKgWPev3tLsfE/HJH/XQd28pED1TeSFAKu0YvIV7S4wmdUsnTzsbLFITkPqHBKo16Ze2SgwtbQ9NtQwMB04Wq07//a5Nn59SPUmy5z6wdpcUDqlrQOTt7YbbzmT96Ghpuo806DU0Kn9T3NB6ZRT72tLn5tbr0rUc/+354zq94UdJQ798rl8HT1RJ6tFslgtcjoNOb//6WqVZP3+l5BTn6fQQItKK5v4LeEMmQUmX+yXWtqvnDL35/4VmPzqNNyZys/PV2Zmptu0rKws5efnS5JqampUWFjo1sZqtSozM9PVpr2577Ui0/nTV56cf6ZBSZIeeL35nf/56rdvmq+zp2MyfVWRa+dgsfzwkKR6p5Tz/fvSnpxe8+mckoIDAxQcYNHRE3Wa/cbWRm1a2h4bWv/lDz88X/n0G+0qO2oalCTpn9tOnv4xC0qS9GXZMY/r8AZvbTfecibvQ0NN1dnaoCT9sP8xC0rSD+9rS58bs6AktZ991pw3t+roiToFB1gUHBigIKv7j1ZDUpDV6vZ58kZQkqQn3/+y2Xm+2C81fE0zD7+zzeuvfS6d12HJbrcrJibGbVpMTIwcDoeOHz+ugwcPqr6+vsk2dnvj88WnVFdXy+FwuD3awt7DlaanOiTpaHW9lud/3ar+a+qNdn89gDftKnO4HdpviidjUuY47jrcfHroOPX8u/IT7eoaJrOaG6p31stqtcpqkT7fW+52zYUn2+PpVhcW60RtvXK3lqqu2rProe78q2fXELbVNUze2m68pTXvwymn19nw2qTWOFpdr6UfNz5d1JTl+V+3+LlpSXvYZ1Ucq1HRvgpZLSd/2ZYkQz8cVTr5XHIaJ98jq9Uqb5/OaeoaJl/slxq+ZkuchvzqGqbzOiydK/Pnz1d4eLjrkZDQNoeBt9vNL6Q8ZXVRSatfo2hvRauX9TeermtL7fYc8uyohqft2kKjWprbe38//dRphdKjP+wIPd0eG3rzPyWqrK7T8dp6nfDwJ8YHOw941O5stvsz4a3txlta8z401LDOtdvPLixJnr8P3nq/fL3PKj1aLafTkMX6QyJp8uKWc3jBy8e7DjWa5ov90pn2VbDniNde+1w7r8NSbGysSkvdT0eVlpYqLCxMoaGhioyMVEBAQJNtYmNj1ZxZs2apoqLC9di7t/WHrc9En9hOHrUbnRzX6tdITghv9bL+xtN1bald4gUdPOrH03ZtoVEtzf0m//104/uLU2M621yzPN0eGxo5IE6dbIEKDQpQiIdHDzIvi/Ko3dls92fCW9uNt7TmfWioYZ0/6+PZl1rMePo+eOv98vU+K6azTVbr91+K+F6TR8Y83N5b4+qeja878sV+6Uz7Skvs4rXXPtfO67CUnp6uvLw8t2lr165Venq6JCk4OFipqalubZxOp/Ly8lxtmmKz2RQWFub2aAsJXTupU7D5W9bZFqBx6T1a1X9wgEU9o9tmXdqDntFhCmrhE+DJmESHhSo+/GSIOP03ylPPL4wIUXRYaGtL9TqzmhsKsAbI6XTKaUgpCREK7xDsmufJ9ni60akXKSQoQNl9YxRoC255AUl/+p/BHrWbel3vM6qltby13XhLa96HU06v8+pLzy4sdbYFaMLVPT1qOy69R4ufm5a0h31WeIdgJXcLl9M4+fNDkiyyqMGBJlkkWS0n3yOn0+n13JR8UddG03yxX2r4mi2xWqSk+Aivvfa55ldhqbKyUkVFRSoqKpJ08tYARUVFKi4+eS+XWbNmafz48a72t912m77++mvNmDFDO3bs0J///Gf9/e9/1z333ONqk5OToxdeeEHLli3T9u3bNXXqVFVVVWnixIltum6eWjA2xXT+U2OSJUm/GHDmv7U9ekO/1pTk1+bf2N90vqdj8oexKQr4/tNkGD88pJPfOlnw/fvSnpxe8+mskmrq6lVTb6hzSKAeHtW3UZuWtseGhlwa6fr//6R3V8/ozgpsYZmspJM/vC+NNv+NtaX53uat7cZbzuR9aKipOm9Jv7jVdZza/5x635pzan5Ln5up15r/4tde9lmPjO6nziGBqqk3VFNXr1pn42vIap1Ot89TXJhnvyy05N6hlzY7zxf7pYavaWb29Ulef+1zya/C0meffaaUlBSlpJzcMeTk5CglJUVz5syRJJWUlLiCkyQlJiZqzZo1Wrt2rQYMGKCnnnpKf/nLX1z3WJKkMWPG6Mknn9ScOXOUnJysoqIi5ebmNrrou70YmhSr58enqrMtwG16Z1uA62u7kvT0TT/xODAFB1jazVdw29p/pSboyf/ur+AA99/1znRM0hIv0IrJV+jCiBC36RdGhLTL2wZIzdccHGBRoEWyWi0KCLBqcGLXJm8bIDW/PZ7u9PssRXay6ZlfpWhaRi91CGp6mYb343k/5/81G4h8cZ8lb2033mK2X7gl/eIzqnPeyL7NBqbmjoicvv95bvygZgNTw/e1pc/N/cP6tKtxbs6lMZ312tQrNTixqwICrJIhBQZY1f/CMPW7MExBgSenNfw85T/wM13cNaTFvn85sFuzgail+yz5Yr/U3GueYrX4320DJD++z1J70tY3pTxl7+FKbbdXqk9sJyV0bf66hX9u2a81W+0a0TdWWf3iJZ38Rk/R3golJ4T7/DB2e+GtMSlzHNeeQ8eUeEGHdnXqzczpNVccq1Hp0WrFdLa5nXoz03B7/GzPYb35nxKNHBCn0akXmS53orZeldV1+r+dpcr9olQ/7x+n65O7Ndv+2XU7tLqoRKOT49rs1JuZ9vZZam6/0Jo6P/6yTGu3l+lnfaJdp+hO9RPb2aZjdc4W9z/vFO3T25tLWnxfW/rctLdxbk5Tn52WPk9/yN2qNzaXalT/GA24KFK520qVnRSj65Lcr50tKj6sj3cd0tU9L2jy1JsZX+yXTr1mbW29vjpQpbTELn516q0hwpIX+CosAQCAc8+vTsMBAAC0NcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACcISAACACb8LS4sWLVL37t0VEhKitLQ0bdiwodm2Q4YMkcViafQYMWKEq82ECRMazc/Ozm6LVQEAAH4g0NcFnImVK1cqJydHixcvVlpamhYuXKisrCzt3LlT0dHRjdq//vrrqqmpcT0/dOiQBgwYoP/+7/92a5edna2XXnrJ9dxms527lQAAAH7Fr44sLViwQJMnT9bEiROVlJSkxYsXq0OHDlqyZEmT7bt27arY2FjXY+3aterQoUOjsGSz2dzadenSpS1WBwAA+AG/CUs1NTUqLCxUZmama5rValVmZqby8/M96uPFF1/U2LFj1bFjR7fp69evV3R0tC677DJNnTpVhw4d8mrtAADAf/nNabiDBw+qvr5eMTExbtNjYmK0Y8eOFpffsGGDtm7dqhdffNFtenZ2tm644QYlJiZq9+7deuCBBzRs2DDl5+crICCgyb6qq6tVXV3teu5wOFqxRgAAwB/4TVg6Wy+++KL69eunwYMHu00fO3as6//9+vVT//79dckll2j9+vXKyMhosq/58+dr3rx557ReAADQPvjNabjIyEgFBASotLTUbXppaaliY2NNl62qqtKrr76qSZMmtfg6PXr0UGRkpHbt2tVsm1mzZqmiosL12Lt3r2crAQAA/I7fhKXg4GClpqYqLy/PNc3pdCovL0/p6emmy65atUrV1dW6+eabW3ydffv26dChQ4qLi2u2jc1mU1hYmNsDAACcn/wmLElSTk6OXnjhBS1btkzbt2/X1KlTVVVVpYkTJ0qSxo8fr1mzZjVa7sUXX9SoUaN0wQUXuE2vrKzUfffdp08//VTffPON8vLyNHLkSPXs2VNZWVltsk4AAKB986trlsaMGaMDBw5ozpw5stvtSk5OVm5uruui7+LiYlmt7vlv586d+vjjj/X+++836i8gIECbN2/WsmXLVF5ervj4eA0dOlQPP/ww91oCAACSJIthGIavi/B3DodD4eHhqqio4JQcAADnGb86DQcAANDWCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAmCEsAAAAm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37Nnj+x2u1ub8PBwpaWlNdsnAAD4cWnVnzupr6/XH/7wB/39739XcXFxo3srHT582CvFNXTw4EHV19c3uiYqJiZGO3bsaHIZu93eZHu73e6af2pac22aUl1drerqatdz/h4eAADnr1YdWZo3b54WLFigMWPGqKKiQjk5ObrhhhtktVr14IMPernE9mf+/PkKDw93PRISEnxdEgAAOEdaFZaWL1+uF154QdOnT1dgYKBuuukm/eUvf9GcOXP06aefertGSVJkZKQCAgJUWlrqNr20tFSxsbFNLhMbG2va/tS/Z9KnJM2aNUsVFRWux969e894fQAAgH9oVViy2+3q16+fJKlTp06qqKiQJF1//fVas2aN96prIDg4WKmpqcrLy3NNczqdysvLU3p6epPLpKenu7WXpLVr17raJyYmKjY21q2Nw+FQQUFBs31Kks1mU1hYmNsDAACcn1oVlrp166aSkhJJ0iWXXKL3339fkrRx40bZbDbvVXeanJwcvfDCC1q2bJm2b9+uqVOnqqqqShMnTpQkjR8/XrNmzXK1/9///V/l5ubqqaee0o4dO/Tggw/qs88+07Rp0yRJFotFd999tx555BG99dZb2rJli8aPH6/4+HiNGjXqnK0HAADwH626wHv06NHKy8tTWlqa7rzzTt1888168cUXVVxcrHvuucfbNbqMGTNGBw4c0Jw5c2S325WcnKzc3FzXBdrFxcWyWn/If1deeaVWrFih3/72t3rggQfUq1cvvfHGG+rbt6+rzYwZM1RVVaUpU6aovLxcV199tXJzcxUSEnLO1gMAAPgPr9xnKT8/X/n5+erVq5d+/vOfe6Muv8J9lgAAOH959aaUP1aEJQAAzl8en4Z76623PO70F7/4RauKAQAAaG88PrLU8Fog0w4tFtXX159VUf6GI0sAAJy/PD6y5HQ6z2UdAAAA7dIZ3Tpg3bp1SkpKavLPe1RUVOjyyy/X//3f/3mtOAAAAF87o7C0cOFCTZ48uclTTeHh4fr1r3+tBQsWeK04AAAAXzujsPSf//xH2dnZzc4fOnSoCgsLz7ooAACA9uKMwlJpaamCgoKanR8YGKgDBw6cdVEAAADtxRmFpQsvvFBbt25tdv7mzZsVFxd31kUBAAC0F2cUloYPH67Zs2frxIkTjeYdP35cc+fO1fXXX++14gAAAHztjO7gXVpaqp/85CcKCAjQtGnTdNlll0mSduzYoUWLFqm+vl6bNm1y/a22HwvuswQAwPnrjP/cybfffqupU6fqn//8p04tarFYlJWVpUWLFikxMfGcFNqeEZYAADh/tfpvwx05ckS7du2SYRjq1auXunTp4u3a/AZhCQCA8xd/SNcLCEsAAJy/zugCbwAAgB8bwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJwhIAAIAJvwlLhw8f1rhx4xQWFqaIiAhNmjRJlZWVpu3vvPNOXXbZZQoNDdVFF12ku+66SxUVFW7tLBZLo8err756rlcHAAD4iUBfF+CpcePGqaSkRGvXrlVtba0mTpyoKVOmaMWKFU22379/v/bv368nn3xSSUlJ+vbbb3Xbbbdp//79eu2119zavvTSS8rOznY9j4iIOJerAgAA/IjFMAzD10W0ZPv27UpKStLGjRs1cOBASVJubq6GDx+uffv2KT4+3qN+Vq1apZtvvllVVVUKDDyZEy0Wi1avXq1Ro0a1uj6Hw6Hw8HBVVFQoLCys1f0AAID2xy9Ow+Xn5ysiIsIVlCQpMzNTVqtVBQUFHvdzKsycCkqn3HHHHYqMjNTgwYO1ZMkS+UF+BAAAbcQvTsPZ7XZFR0e7TQsMDFTXrl1lt9s96uPgwYN6+OGHNWXKFLfpDz30kK677jp16NBB77//vm6//XZVVlbqrrvuarav6upqVVdXu547HI4zWBsAAOBPfBqWZs6cqd///vembbZv337Wr+NwODRixAglJSXpwQcfdJs3e/Zs1/9TUlJUVVWlJ554wjQszZ8/X/PmzTvrugAAQPvn02uWDhw4oEOHDpm26dGjh1555RVNnz5dR44ccU2vq6tTSEiIVq1apdGjRze7/NGjR5WVlaUOHTronXfeUUhIiOnrrVmzRtdff71OnDghm83WZJumjiwlJCRwzRIAAOchnx5ZioqKUlRUVIvt0tPTVV5ersLCQqWmpkqS1q1bJ6fTqbS0tGaXczgcysrKks1m01tvvdViUJKkoqIidenSpdmgJEk2m810PgAAOH/4xTVLffr0UXZ2tiZPnqzFixertrZW06ZN09ixY13fhPvuu++UkZGhl19+WYMHD5bD4dDQoUN17NgxvfLKK3I4HK5ri6KiohQQEKC3335bpaWluuKKKxQSEqK1a9fq0Ucf1b333uvL1QUAAO2IX4QlSVq+fLmmTZumjIwMWa1W3XjjjXr66add82tra7Vz504dO3ZMkrRp0ybXN+V69uzp1teePXvUvXt3BQUFadGiRbrnnntkGIZ69uypBQsWaPLkyW23YgAAoF3zi/sstXfcZwkAgPOXX9xnCQAAwFcISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACb8JiwdPnxY48aNU1hYmCIiIjRp0iRVVlaaLjNkyBBZLBa3x2233ebWpri4WCNGjFCHDh0UHR2t++67T3V1dedyVQAAgB8J9HUBnho3bpxKSkq0du1a1dbWauLEiZoyZYpWrFhhutzkyZP10EMPuZ536NDB9f/6+nqNGDFCsbGx+uSTT1RSUqLx48crKChIjz766DlbFwAA4D8shmEYvi6iJdu3b1dSUpI2btyogQMHSpJyc3M1fPhw7du3T/Hx8U0uN2TIECUnJ2vhwoVNzn/vvfd0/fXXa//+/YqJiZEkLV68WPfff78OHDig4OBgj+pzOBwKDw9XRUWFwsLCznwFAQBAu+UXp+Hy8/MVERHhCkqSlJmZKavVqoKCAtNlly9frsjISPXt21ezZs3SsWPH3Prt16+fKyhJUlZWlhwOh7744gvvrwgAAPA7fnEazm63Kzo62m1aYGCgunbtKrvd3uxyv/rVr3TxxRcrPj5emzdv1v3336+dO3fq9ddfd/XbMChJcj0367e6ulrV1dWu5w6H44zXCQAA+AefhqWZM2fq97//vWmb7du3t7r/KVOmuP7fr18/xcXFKSMjQ7t379Yll1zS6n7nz5+vefPmtXp5AADgP3walqZPn64JEyaYtunRo4diY2NVVlbmNr2urk6HDx9WbGysx6+XlpYmSdq1a5cuueQSxcbGasOGDW5tSktLJcm031mzZiknJ8f13OFwKCEhweM6AACA//BpWIqKilJUVFSL7dLT01VeXq7CwkKlpqZKktatWyen0+kKQJ4oKiqSJMXFxbn6/d3vfqeysjLXab61a9cqLCxMSUlJzfZjs9lks9k8fl0AAOC//OLbcJI0bNgwlZaWavHixa5bBwwcONB164DvvvtOGRkZevnllzV48GDt3r1bK1as0PDhw3XBBRdo8+bNuueee9StWzd9+OGHkk7eOiA5OVnx8fF6/PHHZbfb9T//8z+69dZbz+jWAXwbDgCA85dffBtOOvmttt69eysjI0PDhw/X1Vdfreeff941v7a2Vjt37nR92y04OFgffPCBhg4dqt69e2v69Om68cYb9fbbb7uWCQgI0DvvvKOAgAClp6fr5ptv1vjx493uywQAAH7c/ObIUnvGkSUAAM5ffnNkCQAAwBcISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACYISwAAACb8JiwdPnxY48aNU1hYmCIiIjRp0iRVVlY22/6bb76RxWJp8rFq1SpXu6bmv/rqq22xSgAAwA9YDMMwfF2EJ4YNG6aSkhI999xzqq2t1cSJEzVo0CCtWLGiyfb19fU6cOCA27Tnn39eTzzxhEpKStSpUydJJ8PSSy+9pOzsbFe7iIgIhYSEeFybw+FQeHi4KioqFBYW1oq1AwAA7VWgrwvwxPbt25Wbm6uNGzdq4MCBkqQ//elPGj58uJ588knFx8c3WiYgIECxsbFu01avXq1f/vKXrqB0SkRERKO2AAAAkp+chsvPz1dERIQrKElSZmamrFarCgoKPOqjsLBQRUVFmjRpUqN5d9xxhyIjIzV48GAtWbJEfnKwDQAAtAG/OLJkt9sVHR3tNi0wMFBdu3aV3W73qI8XX3xRffr00ZVXXuk2/aGHHtJ1112nDh066P3339ftt9+uyspK3XXXXc32VV1drerqatdzh8NxBmsDAAD8iU+PLM2cObPZi7BPPXbs2HHWr3P8+HGt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7dtXkjz6DNvt9ia31VPzfmyaGkdJ+tWvfqWLL75Y8fHx2rx5s+6//37t3LlTr7/+uiTG0RsIS2i3hg0b5vp///79lZaWposvvlh///vfFRoa6sPK8GM3duxY1//79eun/v3765JLLtH69euVkZHhw8rapzvuuENbt251u+YQZ665cWx4LVy/fv0UFxenjIwM7d69W5dccklbl3le4jRcG4iMjFRAQECjb3mUlpYqNjbWR1X5n4iICF166aXatWuXYmNjVVNTo/Lycrc2jKm5U2Njti3GxsY2+uJBXV2dDh8+zNg2o0ePHoqMjNSuXbskMYYNTZs2Te+8847+9a9/qVu3bq7pnnyGY2Njm9xWT837MWluHJuSlpYmSW7bI+N4dghLbSA4OFipqanKy8tzTXM6ncrLy1N6eroPK/MvlZWV2r17t+Li4pSamqqgoCC3Md25c6eKi4sZUxOJiYmKjY11GzeHw6GCggLXuKWnp6u8vFyFhYWuNuvWrZPT6XTthOFu3759OnTokOLi4iQxhtLJW1RMmzZNq1ev1rp165SYmOg235PPcHp6urZs2eIWPNeuXauwsDAlJSW1zYr4WEvj2JSioiJJctsef+zjeNZ8fYX5j8Wrr75q2Gw2Y+nSpca2bduMKVOmGBEREW7fToC76dOnG+vXrzf27Nlj/Pvf/zYyMzONyMhIo6yszDAMw7jtttuMiy66yFi3bp3x2WefGenp6UZ6erqPq/a9o0ePGp9//rnx+eefG5KMBQsWGJ9//rnx7bffGoZhGI899pgRERFhvPnmm8bmzZuNkSNHGomJicbx48ddfWRnZxspKSlGQUGB8fHHHxu9evUybrrpJl+tUpszG8OjR48a9957r5Gfn2/s2bPH+OCDD4yf/OQnRq9evYwTJ064+vixj+HUqVON8PBwY/369UZJSYnrcezYMVeblj7DdXV1Rt++fY2hQ4caRUVFRm5urhEVFWXMmjXLF6vkEy2N465du4yHHnrI+Oyzz4w9e/YYb775ptGjRw/jmmuucfXBOJ49wlIb+tOf/mRcdNFFRnBwsDF48GDj008/9XVJ7dqYMWOMuLg4Izg42LjwwguNMWPGGLt27XLNP378uHH77bcbXbp0MTp06GCMHj3aKCkp8WHF7cO//vUvQ1Kjxy233GIYxsnbB8yePduIiYkxbDabkZGRYezc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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "###### class balance under cluster #########\n",
        "\n",
        "#Overall class balance proportions#\n",
        "class_balance = df['Class'].value_counts(normalize=True) # normalising shows the proportions relative to the total\n",
        "\n",
        "print(\"Overall Class Balance:\")\n",
        "print(class_balance)\n",
        "\n",
        "print(end = \"\\n\\n\\n\")\n",
        "\n",
        "#####Grpah to show the mean class value agaisnt the Grouped Info cluster variable#####\n",
        "\n",
        "# Group data by 'Info_cluster' and calculate mean class value\n",
        "mean_class_per_cluster = df.groupby('Info_cluster')['Class'].mean().reset_index()\n",
        "\n",
        "# Scatter plot\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.scatter(mean_class_per_cluster['Info_cluster'], mean_class_per_cluster['Class'], alpha=0.5)\n",
        "plt.title('Info_cluster agaisnt mean class value')\n",
        "plt.xlabel('Info_cluster')\n",
        "plt.ylabel('Mean Class Value')\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n",
        "df.plot(kind='scatter', x='Info_cluster', y='Class', s=32, alpha=.8)\n",
        "plt.gca().spines[['top', 'right',]].set_visible(False)\n",
        "\n",
        "#--- Shows the vast majority of the class varibale is -1"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## EDA Summary\n",
        "\n",
        "*   Most of the dataset is numerical (float64(290), int64(4), object(6))\n",
        "*   It is a high dimensional dataset intially with 300 features\n",
        "*   There are a total of 14993 missing values in the dataset (a single column had over 10,000 missing values and 14 rows have over 250 missing values)\n",
        "*   1 column has a massive differece in scaling\n",
        "*   It is a highly imbalanced dataset - rougly 98% of all classes are \"-1\"\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "1S9grNPhzKtF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Pre-processing**"
      ],
      "metadata": {
        "id": "eXhgxLKvTiRJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Checking missing Values again"
      ],
      "metadata": {
        "id": "xtrTEAip7l7W"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Number of missing values in columns\n",
        "missing_values_columns = df.isnull().sum()\n",
        "\n",
        "# Plot missing values in columns\n",
        "plt.figure(figsize=(10, 6))\n",
        "missing_values_columns.plot(kind='bar')\n",
        "plt.title('Number of Missing Values in Columns')\n",
        "plt.xlabel('Columns')\n",
        "plt.ylabel('Number of Missing Values')\n",
        "plt.xticks(rotation=90)\n",
        "plt.show()\n",
        "\n",
        "#--- this shows that column 'feat_esm1b_148' has over 10,000 missing values and should be removed\n",
        "\n",
        "# Number of missing values in rows\n",
        "missing_values_rows = df.isnull().sum(axis=1)\n",
        "\n",
        "# Plot missing values in rows\n",
        "plt.figure(figsize=(10, 6))\n",
        "missing_values_rows.plot(kind='hist')\n",
        "plt.title('Number of Missing Values in Rows')\n",
        "plt.xlabel('Number of Missing Values')\n",
        "plt.ylabel('Frequency')\n",
        "plt.grid(True)\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "ZwxVWYsu5rRh",
        "outputId": "aefe04b6-7c8e-4739-9cea-bae3734efe9c"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2kAAAKICAYAAADq57I1AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAC570lEQVR4nOzdd3gU1f7H8c/sJrubXklCIITQe1eKSBEQEBEURRSkCiIgKldUrkjxoiJevYi9IXZUVES4Ui4WvIqoKCqICNJFOiSEmnJ+f/CbuVkSJAtBVvN+Pc8+mZzvlHN2Z2b3O+WMZYwxAgAAAAAEBde5rgAAAAAA4H9I0gAAAAAgiJCkAQAAAEAQIUkDAAAAgCBCkgYAAAAAQYQkDQAAAACCCEkaAAAAAAQRkjQAAAAACCIkaQAAAAAQREjSAOAc+/jjj2VZlmbNmnWuq1IsO3bs0JVXXqmEhARZlqWpU6eW+DL69++vihUrlvh8J0yYIMuySny+58KMGTNkWZY2btx4rqtSJMuyNGHChHNdjVP6s9QTQOlCkgagVLB/0Pp8Pv3666+F4m3atFGdOnXOQc3+fG699VYtWLBAY8aM0csvv6xOnTqddFzLsmRZlq6//voi43fddZczzu7du89Wlc+pnJwcJSYmqmXLlicdxxijtLQ0NWrU6A+s2Z/Txx9/rCuuuEIpKSnyeDxKSkpS165d9c4775zrqgFAiSFJA1CqHD16VJMnTz7X1fhT+/DDD9WtWzfddttt6tOnj2rUqPG74/t8Pr399ts6duxYodjrr78un89XqPzZZ5/VmjVrSqzOtrFjx+rw4cMlPt/fExoaqquuukqff/65Nm3aVOQ4S5Ys0datW9WnT58/tG5n0+HDhzV27NgSnef48ePVtm1brVy5UjfccIOeeuopjR49WtnZ2erRo4dee+21El0eAJwrJGkASpUGDRro2Wef1bZt2851Vf5wBw8eLJH57Ny5U7GxscUev1OnTsrKytIHH3zgV/75559rw4YN6tKlS6FpQkND5fV6z7SqhYSEhBSZFJ5tvXv3ljFGr7/+epHx1157TS6XS7169fqDa3b2+Hw+hYSElNj8Zs2apXvuuUdXXnmlVq1apYkTJ2rgwIEaPXq0PvroI82fP1/R0dEltjwAOJdI0gCUKn//+9+Vl5d3yrNpGzdulGVZmjFjRqHYifew2Pc5/fzzz+rTp49iYmJUpkwZ3X333TLGaMuWLerWrZuio6OVkpKihx56qMhl5uXl6e9//7tSUlIUERGhyy67TFu2bCk03rJly9SpUyfFxMQoPDxcrVu31meffeY3jl2nH3/8Uddee63i4uJ+93I7SVq/fr2uuuoqxcfHKzw8XM2aNdO8efOcuH3JqDFGjz/+uHOZ4qmUK1dOrVq1KnSW49VXX1XdunWLvMy0qHvSZs6cqcaNGysqKkrR0dGqW7euHnnkESeek5OjiRMnqmrVqvL5fEpISFDLli21aNGiQu9LQZZlacSIEZo9e7bq1Kkjr9er2rVra/78+YXq9fHHH6tJkyby+XyqXLmynn766WLd53bBBReoYsWKRZ7pycnJ0axZs9S2bVulpqbq+++/V//+/VWpUiX5fD6lpKRo4MCB2rNnz+8uw25LUfdXVaxYUf379/cr279/v2655RalpaXJ6/WqSpUqeuCBB5Sfn+833qne9+LWxX6f1q1bp/79+ys2NlYxMTEaMGCADh06dMr53X333YqPj9f06dMVGhpaKN6xY0ddeumlzv87d+7UoEGDlJycLJ/Pp/r16+vFF1885XJOdj/k7607b731lmrVqqWwsDA1b95cP/zwgyTp6aefVpUqVeTz+dSmTZtC9w/al1n/+OOPatu2rcLDw1WuXDlNmTKl0PIfffRR1a5dW+Hh4YqLi1OTJk04cwj8hZGkAShVMjIy1Ldv37NyNu3qq69Wfn6+Jk+erKZNm2rSpEmaOnWqOnTooHLlyumBBx5QlSpVdNttt2nJkiWFpr/33ns1b9483XHHHRo5cqQWLVqk9u3b+12e9+GHH6pVq1bKysrS+PHjdd9992n//v266KKL9OWXXxaa51VXXaVDhw7pvvvu0+DBg09a9x07dqhFixZasGCBhg0bpnvvvVdHjhzRZZddpnfffVeS1KpVK7388suSpA4dOujll192/j+Va6+9Vu+//76ys7MlSbm5uXrrrbd07bXXFmv6RYsW6ZprrlFcXJweeOABTZ48WW3atPFLTidMmKCJEyeqbdu2euyxx3TXXXepQoUK+uabb045///+978aNmyYevXqpSlTpujIkSPq0aOHX2L07bffqlOnTtqzZ48mTpyoQYMG6Z577tHs2bNPOX/LsnTttdfqhx9+0KpVq/xi8+fP1969e9W7d2+nrevXr9eAAQP06KOPqlevXpo5c6YuueQSGWOK9X6dyqFDh9S6dWu98sor6tu3r6ZNm6YLLrhAY8aM0ahRo5zxivO+B6pnz546cOCA7r//fvXs2VMzZszQxIkTf3eatWvX6qefflL37t0VFRV1ymUcPnxYbdq00csvv6zevXvrwQcfVExMjPr371+sBDMQn376qf72t7+pX79+mjBhglavXq1LL71Ujz/+uKZNm6Zhw4Zp9OjRWrp0qQYOHFho+n379qlTp06qX7++HnroIdWoUUN33HGH35nnZ599ViNHjlStWrU0depUTZw4UQ0aNNCyZctKtC0AgogBgFLghRdeMJLMV199ZX755RcTEhJiRo4c6cRbt25tateu7fy/YcMGI8m88MILheYlyYwfP975f/z48UaSGTJkiFOWm5trypcvbyzLMpMnT3bK9+3bZ8LCwky/fv2cso8++shIMuXKlTNZWVlO+ZtvvmkkmUceecQYY0x+fr6pWrWq6dixo8nPz3fGO3TokMnIyDAdOnQoVKdrrrmmWO/PLbfcYiSZTz/91Ck7cOCAycjIMBUrVjR5eXl+7R8+fHix5muPu3fvXuPxeMzLL79sjDFm3rx5xrIss3HjRqeuu3btcqbr16+fSU9Pd/6/+eabTXR0tMnNzT3psurXr2+6dOnyu/Wxl3ViHT0ej1m3bp1T9t133xlJ5tFHH3XKunbtasLDw82vv/7qlK1du9aEhIQUmmdRVq1aZSSZMWPG+JX36tXL+Hw+k5mZaYw5/nme6PXXXzeSzJIlS5wye53esGGDX1sKrpu29PR0v3XuH//4h4mIiDA///yz33h33nmncbvdZvPmzcaY4r3vJ3Oy7WTgwIF+411++eUmISHhd+f13nvvGUnmX//6V7GWPXXqVCPJvPLKK07ZsWPHTPPmzU1kZKTfdnZiPU9c906sf0GSjNfr9fsMnn76aSPJpKSk+C1nzJgxhT6v1q1bG0nmpZdecsqOHj1qUlJSTI8ePZyybt26+e2fAPz1cSYNQKlTqVIlXXfddXrmmWf022+/ldh8C/Zg6Ha71aRJExljNGjQIKc8NjZW1atX1/r16wtN37dvX7+zBFdeeaXKli2rf//735KkFStWaO3atbr22mu1Z88e7d69W7t379bBgwfVrl07LVmypNClakOHDi1W3f/973/r/PPP97skMjIyUkOGDNHGjRv1448/Fu9NOIm4uDh16tTJuSfrtddeU4sWLZSenl6s6WNjY3Xw4EG/SxeLGmfVqlVau3ZtwPVr3769Kleu7Pxfr149RUdHO59TXl6e/vOf/6h79+5KTU11xqtSpYo6d+5crGXUqlVLDRs21MyZM52ygwcPas6cObr00kud+6nCwsKc+JEjR7R79241a9ZMkop1VrA43nrrLV144YWKi4tz1qPdu3erffv2ysvLc870Fud9D9SJ6+SFF16oPXv2KCsr66TT2LHinEWTjq/PKSkpuuaaa5yy0NBQjRw5UtnZ2frkk09Oo+ZFa9eund/lkU2bNpUk9ejRw6++dvmJ235kZKRfhzEej0fnn3++33ixsbHaunWrvvrqqxKrN4DgRpIGoFQaO3ascnNzS7SnxwoVKvj9HxMTI5/Pp8TExELl+/btKzR91apV/f63LEtVqlRx7mOxk49+/fqpTJkyfq/nnntOR48eVWZmpt88MjIyilX3TZs2qXr16oXKa9as6cTP1LXXXqtFixZp8+bNmj17drEvdZSkYcOGqVq1aurcubPKly+vgQMHFrpn7J577tH+/ftVrVo11a1bV6NHj9b3339frPmf+NlJxxNL+3PauXOnDh8+rCpVqhQar6iyk+ndu7c2bNigzz//XJI0e/ZsHTp0yLnUUZL27t2rm2++WcnJyQoLC1OZMmWcz/HEz/d0rV27VvPnzy+0HrVv317S8fZKxXvfA3Xiex0XFydJRW4TNjuBPXDgQLGWsWnTJlWtWlUul//PnJJcn21FbfeSlJaWVmT5ie0sX758oXvdCq57knTHHXcoMjJS559/vqpWrarhw4ef0SWnAIIfSRqAUqlSpUrq06fPSc+mnawjiLy8vJPO0+12F6tM0mndW2SfJXvwwQe1aNGiIl+RkZF+0xQ8K3OuXXbZZfJ6verXr5+OHj2qnj17FnvapKQkrVixQnPmzNFll12mjz76SJ07d1a/fv2ccVq1aqVffvlF06dPV506dfTcc8+pUaNGeu655045/5L8nH7PNddcI5fL5XT48NprrykuLk6XXHKJM07Pnj317LPPaujQoXrnnXe0cOFCJzE68UxpcZ243ubn56tDhw4nXY969OghqXjve6BO5722H/Ngd8hxNgW67Z+sPcVtZ3HGq1mzptasWaOZM2eqZcuWevvtt9WyZUuNHz++yGkB/PmVXN+4APAnM3bsWL3yyit64IEHCsXso/v79+/3Ky/JI/AnOvEyPWOM1q1bp3r16kmSczledHS0c8ajpKSnpxf5XLKffvrJiZ+psLAwde/eXa+88oo6d+5c6AzjqXg8HnXt2lVdu3ZVfn6+hg0bpqefflp33323czYrPj5eAwYM0IABA5Sdna1WrVppwoQJJ32YdnElJSXJ5/Np3bp1hWJFlZ1Mamqq2rZtq7feekt33323Fi1apP79+8vj8Ug6fpZl8eLFmjhxosaNG+dMV9xLOOPi4gqts8eOHSt0IKJy5crKzs4u1npUnPf9bKtWrZqqV6+u9957T4888kihgxEnSk9P1/fff6/8/Hy/s2nFWZ+Leg+ls7vtF0dERISuvvpqXX311Tp27JiuuOIK3XvvvRozZsw5eawEgLOLM2kASq3KlSurT58+evrpp7V9+3a/WHR0tBITEwv1wvjEE0+ctfq89NJLfpdzzZo1S7/99ptzz1Pjxo1VuXJl/fOf/3R6SSxo165dp73sSy65RF9++aWWLl3qlB08eFDPPPOMKlasqFq1ap32vAu67bbbNH78eN19990BTXdi9/Mul8tJXo8ePVrkOJGRkapSpYoTPxNut1vt27fX7Nmz/XoFXbduXaHnv51K7969tXPnTt1www3Kycnxu9TRPqty4tmWqVOnFmvelStXLrTOPvPMM4XOAvXs2VNLly7VggULCs1j//79ys3NlVS89/2PMnHiRO3Zs0fXX3+9U7+CFi5cqLlz50o6vj5v375db7zxhhPPzc3Vo48+qsjISLVu3fqky6lcubIyMzP9LpX97bffnF5Oz4UTPwePx6NatWrJGKOcnJxzVCsAZxNn0gCUanfddZdefvllrVmzRrVr1/aLXX/99Zo8ebKuv/56NWnSREuWLNHPP/981uoSHx+vli1basCAAdqxY4emTp2qKlWqOF3nu1wuPffcc+rcubNq166tAQMGqFy5cvr111/10UcfKTo6Wu+///5pLfvOO+/U66+/rs6dO2vkyJGKj4/Xiy++qA0bNujtt98udG/P6apfv77q168f8HTXX3+99u7dq4suukjly5fXpk2b9Oijj6pBgwbOfUa1atVSmzZt1LhxY8XHx+vrr7/WrFmzNGLEiBKp+4QJE7Rw4UJdcMEFuvHGG5WXl6fHHntMderU0YoVK4o9nx49emjYsGF67733lJaWplatWjmx6OhotWrVSlOmTFFOTo7KlSunhQsXasOGDcWa9/XXX6+hQ4eqR48e6tChg7777jstWLCg0FnL0aNHOx2W9O/fX40bN9bBgwf1ww8/aNasWdq4caMSExOL9b7/Ua6++mr98MMPuvfee/Xtt9/qmmuuUXp6uvbs2aP58+dr8eLFzmWkQ4YM0dNPP63+/ftr+fLlqlixombNmqXPPvtMU6dO/d0OSHr16qU77rhDl19+uUaOHKlDhw7pySefVLVq1Uqs45ZAXXzxxUpJSdEFF1yg5ORkrV69Wo899pi6dOlS7M5UAPy5kKQBKNWqVKmiPn36FPmQ23HjxmnXrl2aNWuW3nzzTXXu3FkffPCBkpKSzkpd/v73v+v777/X/fffrwMHDqhdu3Z64oknFB4e7ozTpk0bLV26VP/4xz/02GOPKTs7WykpKWratKluuOGG0152cnKyPv/8c91xxx169NFHdeTIEdWrV0/vv/++unTpUhLNOyP2/YNPPPGE9u/fr5SUFF199dWaMGGCk0COHDlSc+bM0cKFC3X06FGlp6dr0qRJGj16dInUoXHjxvrggw9022236e6771ZaWpruuecerV692rmMrjiio6PVtWtXvfXWW7rmmmsK3QP12muv6aabbtLjjz8uY4wuvvhiffDBB369Sp7M4MGDtWHDBj3//POaP3++LrzwQi1atEjt2rXzGy88PFyffPKJ7rvvPr311lt66aWXFB0drWrVqmnixIlOJxfFed//SJMmTdJFF12kadOm6cknn9TevXsVFxenZs2a6b333tNll10m6filtR9//LHuvPNOvfjii8rKylL16tX1wgsvFHqo94kSEhL07rvvatSoUbr99tuVkZGh+++/X2vXrj1nSdoNN9ygV199VQ8//LCys7NVvnx5jRw5UmPHjj0n9QFw9lmmpO+KBgCgFOnevftpd/0PAEBRuCcNAIBiOnz4sN//a9eu1b///W+1adPm3FQIAPCXxJk0AACKqWzZsurfv78qVaqkTZs26cknn9TRo0f17bffFnrOHQAAp4t70gAAKKZOnTrp9ddf1/bt2+X1etW8eXPdd999JGgAgBLFmTQAAAAACCLckwYAAAAAQYQkDQAAAACCCPeklZD8/Hxt27ZNUVFRhZ55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alN0dLSJi4sz1apVMzExMeaee+4x77zzjqlVq9Zp5RWWMX9gH5Z/YS+//LKeeuoprV+/Xvfff782bNigRYsWKSoqShkZGQoPD9ff//53hYSEKDY21m/alStX6o033nC63J01a5aeeeYZpaamyuVyaevWrUpISNDtt9+uX375Ra+99ppWrFih9PR0JSUlacOGDdq9e7f27t2rvLw8DRkyROeff77i4uKUkZHhLOf111/X66+/rmPHjumTTz7R2LFj9dtvv6ls2bLaunWrfvrpJ4WGhqpZs2YaMGCAfvrpJz333HNasWKF8vPzFRYWpiNHjig0NFTS8Xt97rrrLlWpUkUNGjTwa9Pdd9+tWbNmad++fdqxY4cmTpyo119/XeXLl5fL5dK+ffsUHh6ujh07au/evfr888+VmZmpnJwcGWOce+IOHjwoSRowYICaNGlSaFn2cowxWrNmjW644QatX79e6enp2rp1qzZs2CBJqlu3roYOHaqff/5ZzzzzjHMfUkxMjCQ59xH4fD6NHz/+nLdp7ty5uu222/S3v/1NO3bs0FNPPaWpU6eqfPny2rJlS5Ft2rRpk0JDQ5WRkaHIyEi53W4dOnRIHo9HDz74YKH1oeA6sXHjRq1bt87phr5ChQrOfUxJSUnq0KGDsrOztWjRImVmZurQoUPKzs5Wdna2jhw5okOHDsnlcqlv374l2qbNmzcrISFBjRo1ktvt1u7du/Xbb78pNzdXI0eOLNZ6PmTIEK1evfqUbcrNzVVubq4sy5IxRnv27FFeXp6GDRt20uW88847uuuuu9S3b1/98ssveuuttzR16lRVqFBBv/zyS5Hb048//qioqChZlqVNmzZp3759ysvLk9frVdeuXdWgQQO1aNFCzZs317Zt25Senq6ePXtq4cKFCg0N1e7du3XZZZfpp59+Unp6urZs2aJdu3bJGKOMjAxdd9112rZtm6ZPn659+/YpNDRUcXFx8vl8OnLkiHJzc9WhQwddfvnlJfo5RUZGKioqSrt373ba5PF4dNlll5V4m9xut0JDQ3X06FG5XC75fD6FhYXplltuUYsWLdSqVSvl5OQUWlZOTo4OHTqkgQMHavbs2UpISJBlWTp27JhcLpdatmypffv2afny5crOzpbL5VJeXp5zn0NeXp5CQ0PVrVu3P22bQkJC5Ha75fV6FRoaqgMHDkiSBg0aVOxtt3nz5qpdu/bv7mN/+eUXScfvxTp48KBcLpfCwsIUERGhm266KejaVNz1PDY2VhUqVNChQ4e0f/9+7d+/X5LUoUMHXXvttbrkkktK5HsjKytL2dnZyszMdO6TsSxL559/vurWravu3burS5cuOnjwoL7++mvddttt+vrrr9WjRw/NmTNHOTk5GjRokF566SW5XC7l5OTI7XarTJky6tKlizIzM/X2228rLy9Pbrfbud/G3nZDQkLUvXv3M1rPK1asqPj4eOeeevP/jyyx7+OxNW3atMTb5HK5FBERoYMHD8ocPyFRaFlt2rTR119/rdatW+u8887T119/7UzTtGlT/fTTT0pOTtbmzZt17Nixky6rIOv/718KCwvTtddeW6hNH3/8sebOnauvv/5aoaGhQdsmy7Lk9XqVm5srl8vl3Kc5atSoEt12jTE6duyYcz/5X6FNXq9Xqampuvzyy3X33Xfr66+/1pEjR5x7/gNyWqkd/DzxxBMmMTHRDBs2zHi9XvPLL78YY4y56aabTEJCghkzZow5evRooeluvPFGs2vXrpMOn078ZNOcK3l5eWb//v0mPz//L7Gcv/Ky/ih/xTb9UQ4cOGBWrFhhjhw5ctaX9Ud9TnabitpHnq1lne3376/YJmP+mutEsH9HHTt2zGzbts1s27bNHDt2rFjTbN682cyePdtkZ2f/7niHDx82Bw4cCKg+BZ3u53Q6bdqyZctptSnQZdnLKc77UnBZwdym4q4PRS0rUKe7PzrdzymY21QSOJNWAmrVqqX77rtP9957r1auXKlVq1Y55cYYVahQQV26dNHUqVP9pouOjtaKFStUqVKlIocbNGgQcNwuS0tLU1xcnL755hv5fD5VqFBBubm52rZtm99wampqobIKFSooJydHv/3220njBYfPth07dujo0aOqUKGCM+z1eotVFkj8hRde0PDhw5WYmKiJEycWGn788cdLLJ6Tk+OckbSHiyo73fjhw4f13//+V5s3b1ZaWpry8/P166+/qnz58jLGaPPmzdq3b5/i4+NVoUIFGWP066+/OuOeLF6+fHnt379fmZmZ2r9/v0JCQlSvXj3VrVtXycnJkqTdu3c7R2Xt4aLKihOXjvfetGnTJqWlpWnLli0qW7as3nvvPf3666+KiIhQdHS0KlSooM2bN2vXrl3q1q2bvvjiC/36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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2QAAAIjCAYAAABswtioAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABaeklEQVR4nO3deXgNd///8dcJWQTZLFkqiH2LpbSaWqoVSVBFdUHUltIlbpTS6q3W3rW01Nq63XeL9kZbLbpaTi2NJbVVqhRFQ9qSUFvEEpHM7w+/zNcRS6RhIuf5uK5cl/OZz5l5z7xP1KuzHJthGIYAAAAAAHeci9UFAAAAAICzIpABAAAAgEUIZAAAAABgEQIZAAAAAFiEQAYAAAAAFiGQAQAAAIBFCGQAAAAAYBECGQAAAABYhEAGAAAAABYhkAHAXWzt2rWy2Wz67LPPrC4lV1JSUvTEE0+oVKlSstlsmjJlSr5vo2fPnqpYsWK+r3fUqFGy2Wz5vl4rzJ07VzabTQcPHrS6lGuy2WwaNWqU1WUAwB1BIAOAm8j+x6uHh4f+/PPPHMtbtGihOnXqWFDZ3eell17SihUrNGzYMH300UeKioq67lybzSabzaZnn332msv/+c9/mnP++uuv21WypTIyMlS6dGk1bdr0unMMw1BwcLDuvffeO1jZ3aVnz57mZ8Vms8nd3V3VqlXTiBEjdOHCBavLA+DkCGQAkEvp6ekaP3681WXc1VavXq327dvr5ZdfVrdu3VSjRo0bzvfw8NDnn3+uixcv5li2cOFCeXh45Bj/z3/+o7179+ZbzdmGDx+u8+fP5/t6b8TV1VVPPvmkNm7cqEOHDl1zTlxcnP744w9169btjtZ2O50/f17Dhw/P13W6u7vro48+0kcffaTJkyerYsWKGjt2rGJiYvJ1OwBwqwhkAJBL9evX13/+8x8dPnzY6lLuuLNnz+bLeo4ePSofH59cz4+KilJqaqqWLVvmML5x40YlJiaqbdu2Od7j6uoqd3f3v1tqDkWLFr1mALzdoqOjZRiGFi5ceM3lCxYskIuLizp37nyHK7t9PDw8VLRo0XxdZ9GiRdWtWzd169ZNsbGxWrFihR544AEtXLhQKSkp+botALgVBDIAyKXXXntNmZmZNz1LdvDgQdlsNs2dOzfHsqvvjcm+L+nXX39Vt27d5O3trTJlyuj111+XYRj6/fff1b59e3l5eSkgIECTJk265jYzMzP12muvKSAgQMWLF9djjz2m33//Pce8TZs2KSoqSt7e3vL09NRDDz2kDRs2OMzJrumXX35R165d5evre8NL5iTpt99+05NPPik/Pz95enrqgQce0DfffGMuz77s0zAMzZw507x07GbuueceNW/eXAsWLHAYnz9/vkJDQ695qei17iH7+OOP1bBhQ5UsWVJeXl4KDQ3V1KlTzeUZGRkaPXq0qlatKg8PD5UqVUpNmzaV3W7PcVyuZLPZ1K9fPy1dulR16tSRu7u7ateureXLl+eoa+3atWrUqJE8PDxUuXJl/fvf/87VfWlNmjRRxYoVcxyD7Lo/++wzPfzwwwoKCtKOHTvUs2dPVapUSR4eHgoICFDv3r11/PjxG24je1+udd9WxYoV1bNnT4exU6dOaeDAgQoODpa7u7uqVKmiCRMmKCsry2HezY57bmvJPk779+9Xz5495ePjI29vb/Xq1Uvnzp276fqut42mTZvKMAz99ttvDsveffdd1a5dW+7u7goKClJsbKxOnTplLp82bZqKFCniMDZp0iTZbDYNGjTIHMvMzFTJkiX1yiuvmGN5PSYACi8CGQDkUkhIiLp3735bzpI9/fTTysrK0vjx49W4cWO98cYbmjJlilq1aqV77rlHEyZMUJUqVfTyyy8rLi4ux/v/9a9/6ZtvvtErr7yi/v37y263Kzw83OESu9WrV6t58+ZKTU3VyJEj9eabb+rUqVN65JFHtHnz5hzrfPLJJ3Xu3Dm9+eab6tOnz3VrT0lJ0YMPPqgVK1boxRdf1L/+9S9duHBBjz32mJYsWSJJat68uT766CNJUqtWrcxLx3Kja9eu+uqrr5SWliZJunTpkhYtWqSuXbvm6v12u11dunSRr6+vJkyYoPHjx6tFixYOQXTUqFEaPXq0Hn74Yc2YMUP//Oc/Vb58ef344483Xf/69ev14osvqnPnzpo4caIuXLigTp06OYSg7du3KyoqSsePH9fo0aMVExOjMWPGaOnSpTddv81mU9euXfXzzz9r165dDsuWL1+uEydOKDo62tzX3377Tb169dL06dPVuXNnffzxx2rTpo0Mw8jV8bqZc+fO6aGHHtL//vc/de/eXdOmTVOTJk00bNgwhzCSm+N+q5566imdOXNG48aN01NPPaW5c+dq9OjReV5f9kNNfH19zbFRo0YpNjZWQUFBmjRpkjp16qR///vfioiIUEZGhiSpWbNmysrK0vr16833rVu3Ti4uLlq3bp05tn37dqWlpal58+aSbs8xAVAIGACAG5ozZ44hydiyZYtx4MABo2jRokb//v3N5Q899JBRu3Zt83ViYqIhyZgzZ06OdUkyRo4cab4eOXKkIcno27evOXbp0iWjXLlyhs1mM8aPH2+Onzx50ihWrJjRo0cPc2zNmjWGJOOee+4xUlNTzfFPP/3UkGRMnTrVMAzDyMrKMqpWrWpERkYaWVlZ5rxz584ZISEhRqtWrXLU1KVLl1wdn4EDBxqSjHXr1pljZ86cMUJCQoyKFSsamZmZDvsfGxubq/Vmzz1x4oTh5uZmfPTRR4ZhGMY333xj2Gw24+DBg2atx44dM9/Xo0cPo0KFCubrAQMGGF5eXsalS5euu6169eoZbdu2vWE92du6ukY3Nzdj//795thPP/1kSDKmT59ujrVr187w9PQ0/vzzT3Ns3759RtGiRXOs81p27dplSDKGDRvmMN65c2fDw8PDOH36tGEYl/t5tYULFxqSjLi4OHMs+zOdmJjosC9XfjazVahQweEzN3bsWKN48eLGr7/+6jDv1VdfNYoUKWIkJSUZhpG743491/s96d27t8O8jh07GqVKlbrp+nr06GEUL17cOHbsmHHs2DFj//79xttvv23YbDajTp065u/E0aNHDTc3NyMiIsLhcztjxgxDkvHBBx8YhmEYmZmZhpeXlzF06FDDMC7/fpUqVcp48sknjSJFihhnzpwxDMMwJk+ebLi4uBgnT57828cEQOHFGTIAuAWVKlXSM888o9mzZ+vIkSP5tt4rnyRYpEgRNWrUSIZhODxwwMfHR9WrV89xeZUkde/eXSVLljRfP/HEEwoMDNS3334rSUpISNC+ffvUtWtXHT9+XH/99Zf++usvnT17Vi1btlRcXFyOy82ef/75XNX+7bff6v7773e4rLFEiRLq27evDh48qF9++SV3B+E6fH19FRUVZd5DtWDBAj344IOqUKFCrt7v4+Ojs2fPOlx+eK05u3bt0r59+265vvDwcFWuXNl8XbduXXl5eZl9yszM1HfffacOHTooKCjInFelShW1bt06V9uoVauWGjRooI8//tgcO3v2rL788ks9+uij8vLykiQVK1bMXH7hwgX99ddfeuCBByQpV2f7cmPRokVq1qyZfH19zc/RX3/9pfDwcGVmZppncHNz3G/V1Z/JZs2a6fjx40pNTb3pe8+ePasyZcqoTJky5tnmJk2a6IsvvjAvG/3uu+908eJFDRw4UC4u//dPpD59+sjLy8u8DNfFxUUPPvigua+7d+/W8ePH9eqrr8owDMXHx0u6fNasTp065n2Tt+OYALj7EcgA4BYNHz5cly5dytcnLpYvX97htbe3tzw8PFS6dOkc4ydPnszx/qpVqzq8ttlsqlKlinlJVnbQ6NGjh/mP0uyf//73v0pPT9fp06cd1hESEpKr2g8dOqTq1avnGK9Zs6a5/O/q2rWr7Ha7kpKStHTp0lxfrihJL774oqpVq6bWrVurXLly6t27d457vMaMGaNTp06pWrVqCg0N1ZAhQ7Rjx45crf/q3kmXQ2R2n44eParz58+rSpUqOeZda+x6oqOjlZiYqI0bN0qSli5dqnPnzpmXK0rSiRMnNGDAAPn7+6tYsWIqU6aM2cer+5tX+/bt0/Lly3N8jsLDwyVd3l8pd8f9Vl19rLMvNbzW78TVPDw8ZLfbZbfbNWfOHNWsWVNHjx51CLHZn9WrP89ubm6qVKmSw2e5WbNm2rZtm86fP69169YpMDBQ9957r+rVq2detrh+/Xo1a9bMfM/tOCYA7n75+wgjAHAClSpVUrdu3TR79my9+uqrOZZf7yENmZmZ111nkSJFcjUmKU/3AmWf/XrrrbdUv379a84pUaKEw+sr/6Fqtccee0zu7u7q0aOH0tPT9dRTT+X6vWXLllVCQoJWrFihZcuWadmyZZozZ466d++uefPmSbp8j9uBAwf0xRdfaOXKlfrvf/+rd955R7Nmzbru96Bly88+3UiXLl00dOhQ8wzhggUL5OvrqzZt2phznnrqKW3cuFFDhgxR/fr1VaJECWVlZSkqKirHGdDcuvpzm5WVpVatWmno0KHXnF+tWjVJuTvut+rvHOsiRYqYoVGSIiMjVaNGDT333HP68ssvb7mWpk2bKiMjQ/Hx8Vq3bp0ZvJo1a6Z169Zpz549OnbsmEMgux3HBMDdjzNkAJAH2WfJJkyYkGNZ9v+1v/IJbFL+nCm6nqsvtTMMQ/v37zefNph9SZ2Xl5fCw8Ov+ePq6pqnbVeoUOGa3/u1Z88ec/nfVaxYMXXo0EFr165Vq1atcpw5vBk3Nze1a9dO7777rg4cOKDnnntOH374ofbv32/O8fPzU69evbRw4UL9/vvvqlu37jWfOnirypYtKw8PD4dtZbvW2PUEBQXp4Ycf1qJFi5SSkiK73a4nnnhCbm5uki6fJVq1apVeffVVjR49Wh07dlSrVq1UqVKlXK3f19c3x2f24sWLOS7NrVy5stLS0q77ObryLFZujrtVAgMD9dJLL+mrr77SDz/8IOn/PqtXf54vXryoxMREh8/y/fffLzc3N61bt84hkDVv3lybNm3SqlWrzNdXKsjHBIA1CGQAkAeVK1dWt27d9O9//1vJyckOy7y8vFS6dOkcT0N89913b1s9H374oc6cOWO+/uyzz3TkyBHzHqWGDRuqcuXKevvtt82nFV7p2LFjed52mzZttHnzZvO+Geny/TqzZ89WxYoVVatWrTyv+0ovv/yyRo4cqddff/2W3nf1I99dXFxUt25dSZe/7Ptac0qUKKEqVaqYy/+O7DMzS5cudXg65/79+3N8v9rNREdH6+jRo3ruueeUkZHhcLli9tmjq88WTZkyJVfrrly5co7P7OzZs3OcIXvqqacUHx+vFStW5FjHqVOndOnSJUm5O+5W+8c//iFPT0/z8uPw8HC5ublp2rRpDsfx/fff1+nTpx2+987Dw0P33XefFi5cqKSkJIczZOfPn9e0adNUuXJlBQYGmu+5G44JgDuPSxYBII/++c9/6qOPPtLevXtVu3Zth2XPPvusxo8fr2effVaNGjVSXFycfv3119tWi5+fn5o2bapevXopJSVFU6ZMUZUqVczH1bu4uOi///2vWrdurdq1a6tXr16655579Oeff2rNmjXy8vLSV199ladtv/rqq1q4cKFat26t/v37y8/PT/PmzVNiYqI+//xzh4cj/B316tVTvXr1bvl9zz77rE6cOKFHHnlE5cqV06FDhzR9+nTVr1/fvM+tVq1aatGihRo2bCg/Pz9t3bpVn332mfr165cvtY8aNUorV65UkyZN9MILLygzM1MzZsxQnTp1lJCQkOv1dOrUSS+++KK++OILBQcHO5x98fLyUvPmzTVx4kRlZGTonnvu0cqVK5WYmJirdT/77LN6/vnn1alTJ7Vq1Uo//fSTVqxYkeNs5JAhQ8yHifTs2VMNGzbU2bNn9fPPP+uzzz7TwYMHVbp06Vwdd6uVKlVKvXr10rvvvqvdu3erZs2aGjZsmEaPHq2oqCg99thj2rt3r959913dd9996tatm8P7mzVrpvHjx8vb21uhoaGSLp8RrV69uvbu3Zvj+9vuhmMC4M7jDBkA5FGVKlVy/AMt24gRIxQTE6PPPvtMQ4cOVWZm5i2fDbkVr732mtq2batx48Zp6tSpatmypVatWiVPT09zTosWLRQfH69GjRppxowZ+sc//qG5c+cqICBAL730Up637e/vr40bN6pVq1aaPn26hg0bJjc3N3311Vfq2LFjfuze39KtWzd5eHjo3Xff1Ysvvqh58+bp6aef1rJly8yw2L9/fx08eFDjxo1T//799f333+uNN9647hdx36qGDRtq2bJl8vX11euvv673339fY8aMUcuWLeXh4ZHr9Xh5ealdu3aSLt9TdvX9igsWLFBkZKRmzpypYcOGydXVNdefuz59+uiVV15RXFycBg8erMTERNntdhUvXtxhnqenp77//nsNGTJEa9eu1YABAzR+/Hjt27dPo0ePlre3t6TcHfeCYNCgQXJxcTEvPx41apRmzJihpKQkvfTSS/r000/Vt29frVy5MsdlvdlnxR588EGHfbrybNmV7pZjAuDOshn5fdcxAADIlQ4dOuT5cfsAgMKB/x0DAMAdcP78eYfX+/bt07fffqsWLVpYUxAAoEDgDBkAAHdAYGCgevbsaX6f1Xvvvaf09HRt3749x/fIAQCcBw/1AADgDoiKitLChQuVnJwsd3d3hYWF6c033ySMAYCT4wwZAAAAAFiEe8gAAAAAwCIEMgAAAACwCPeQ5ZOsrCwdPnxYJUuWzPG9MAAAAACch2EYOnPmjIKCgm76PYMEsnxy+PBhBQcHW10GAAAAgALi999/V7ly5W44h0CWT0qWLCnp8kH38vKytJaMjAytXLlSERERcnV1tbQW3Dn03fnQc+dDz50TfXc+9Pzul5qaquDgYDMj3AiBLJ9kX6bo5eVVIAKZp6envLy8+CV2IvTd+dBz50PPnRN9dz70vPDIza1MPNQDAAAAACxCIAMAAAAAixDIAAAAAMAiBDIAAAAAsAiBDAAAAAAsQiADAAAAAIsQyAAAAADAIgQyAAAAALAIgQwAAAAALEIgAwAAAACLEMgAAAAAwCIEMgAAAACwCIEMAAAAACxCIAMAAAAAixDIAAAAAMAiBDIA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8W3btikjI0Ph4eHmWI0aNVS+fHnFx8frgQceUHx8vEJDQ+Xv72/OiYyM1AsvvKBdu3apQYMGio+Pd1hH9pwrL428Wnp6utLT083XqampkqSMjAxlZGT83V3+W7K37+5iWFpHQWV1f26X7P0qrPuHnOi586Hnzom+Ox96fve7ld4V+ED28ccf68cff9SWLVtyLEtOTpabm5t8fHwcxv39/ZWcnGzOuTKMZS/PXnajOampqTp//ryKFSuWY9vjxo3T6NGjc4yvXLlSnp6eud/B22hsoyyrSyiQvv32W6tLuK3sdrvVJeAOo+fOh547J/rufOj53evcuXO5nlugA9nvv/+uAQMGyG63y8PDw+pyHAwbNkyDBg0yX6empio4OFgRERHy8vKysLLLidxut+v1rS5Kz7JZWktBtHNUpNUl3BbZfW/VqpVcXV2tLgd3AD13PvTcOdF350PP737ZV8/lRoEOZNu2bdPRo0d17733mmOZmZmKi4vTjBkztGLFCl28eFGnTp1yOEuWkpKigIAASVJAQIA2b97ssN7spzBeOefqJzOmpKTIy8vrmmfHJMnd3V3u7u45xl1dXQvML056lk3pmQSyqxWU/twuBekziDuDnjsfeu6c6Lvzoed3r1vpW4F+qEfLli31888/KyEhwfxp1KiRoqOjzT+7urpq1apV5nv27t2rpKQkhYWFSZLCwsL0888/6+jRo+Ycu90uLy8v1apVy5xz5Tqy52SvAwAAAABuhwJ9hqxkyZKqU6eOw1jx4sVVqlQpczwmJkaDBg2Sn5+fvLy89I9//ENhYWF64IEHJEkRERGqVauWnnnmGU2cOFHJyckaPny4YmNjzTNczz//vGbMmKGhQ4eqd+/eWr16tT799FN98803d3aHAQAAADiVAh3IcuOdd96Ri4uLOnXqpPT0dEVGRurdd981lxcpUkRff/21XnjhBYWFhal48eLq0aOHxowZY84JCQnRN998o5deeklTp05VuXLl9N///leRkYXzXiMAAAAABcNdF8jWrl3r8NrDw0MzZ87UzJkzr/ueChUq3PTJei1atND27dvzo0QAAAAAyJUCfQ8ZAAAAABRmBDIAAAAAsAiBDAAAAAAsQiADAAAAAIsQyAAAAADAIgQyAAAAALAIgQwAAAAALEIgAwAAAACLEMgAAAAAwCIEMgAAAACwCIEMAAAA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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Dealing with Missing Values by removing columns and rows with missing values"
      ],
      "metadata": {
        "id": "luzwvSgK7jxK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define thresholds for the percentage of missing values in columns and rows\n",
        "threshold_column = 0.5\n",
        "threshold_row = 0.5\n",
        "\n",
        "# Calculate the percentage of missing values in each column and row\n",
        "missing_percentage_column = df.isnull().mean()\n",
        "missing_percentage_row = df.isnull().mean(axis=1)\n",
        "\n",
        "# Get the list of columns and rows to drop\n",
        "columns_to_drop = missing_percentage_column[missing_percentage_column > threshold_column].index.tolist()\n",
        "rows_to_drop = missing_percentage_row[missing_percentage_row > threshold_row].index.tolist()\n",
        "\n",
        "# Remove columns and rows with mostly missing values from the dataset\n",
        "cleaned_df = df.drop(columns=columns_to_drop, index=rows_to_drop)\n",
        "\n",
        "print(\"\\n\\n\\n\")\n",
        "# Print the list of columns and rows dropped\n",
        "print(\"Columns dropped:\", columns_to_drop)\n",
        "print(\"Rows dropped:\", rows_to_drop)\n",
        "print(\"\\n\\n\\n\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fIKKk7AD5riJ",
        "outputId": "d775e2ec-7760-4171-a044-f25bac7211f4"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "Columns dropped: ['feat_esm1b_148']\n",
            "Rows dropped: [100, 1139, 2775, 3371, 5676, 5795, 7473, 7727, 8958, 9192, 9718, 10507, 11048, 12239]\n",
            "\n",
            "\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Plot missing values again to determine if missing values are gone"
      ],
      "metadata": {
        "id": "BVW18G0l70WW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Plot the count of missing values per column on a scatter plot\n",
        "\n",
        "missing_values = cleaned_df.isnull().sum()\n",
        "plt.figure(figsize=(10, 6)) # the number of inches\n",
        "plt.scatter(missing_values.index, missing_values.values, color='blue')\n",
        "plt.title('Count of Missing Values per Column')\n",
        "plt.xlabel('Columns')\n",
        "plt.ylabel('Count of Missing Values')\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n",
        "\n",
        "# Check for missing values per row\n",
        "missing_values_per_row = cleaned_df.isnull().sum(axis=1)\n",
        "\n",
        "# Plot the count of missing values per row on a scatter plot\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.scatter(cleaned_df.index, missing_values_per_row, color='red')\n",
        "plt.title('Count of Missing Values per Row')\n",
        "plt.xlabel('Rows')\n",
        "plt.ylabel('Count of Missing Values')\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n",
        "\n",
        "# Check for missing values in the cleaned dataset\n",
        "remaining_missing_values = cleaned_df.isnull().sum().sum()\n",
        "\n",
        "if remaining_missing_values == 0:\n",
        "    print(\"No remaining missing values in the cleaned dataset.\")\n",
        "else:\n",
        "    print(f\"There are {remaining_missing_values} remaining missing values in the cleaned dataset.\")\n",
        "\n",
        "print(\"\\n\\n\\n\")\n",
        "\n",
        "\n",
        "# set the df to cleaned df\n",
        "df = cleaned_df\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "zSdRbCgj5IWU",
        "outputId": "968897e7-8f9d-4458-ce03-24038cfc3b1d"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3gAAAIjCAYAAABRULnOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABXTUlEQVR4nO3dd3hUZf738c8kmTRCCCUhhRJAehFFQcCVqgFRQRCkKIiADVwgCP6sgFguXRFQQKyIC1kVxOBaggjIriaAFAsKCFKlhJYMkJB+P3/wZJYhIczAhJDD+3Vd5yJzn3O+8z2TyTgfT7MZY4wAAAAAAOWeT1k3AAAAAADwDgIeAAAAAFgEAQ8AAAAALIKABwAAAAAWQcADAAAAAIsg4AEAAACARRDwAAAAAMAiCHgAAAAAYBEEPAAAAACwCAIeAFzh8vLyNGHCBNWsWVM+Pj7q1auX15/jgw8+kM1m065du7xa97vvvpPNZtN3333n1bplYdeuXbLZbPrggw/KupUripXeQwAgEfAAQJL0559/6sEHH1TdunUVGBio0NBQtW/fXjNmzNCpU6fKuj1J0uzZs0vly//777+vf/zjH7rrrrs0b948jR079pzLduzYUTabTfXr1y92/rJly2Sz2WSz2bRo0SKv93q5uOOOOxQcHKwTJ06cc5lBgwbJ399fR48evYSdWV9+fr7mzp2rjh07qkqVKgoICFBsbKyGDh2qdevWlXV7AFDm/Mq6AQAoa19++aX69u2rgIAADR48WM2aNVNOTo6+//57jR8/Xr/99pvefvvtsm5Ts2fPVrVq1XTfffd5te6KFSsUExOjadOmubV8YGCgtm/frrVr16p169Yu8xYsWKDAwEBlZWW5jN97773q37+/AgICvNa3JN100006deqU/P39vVr3fAYNGqR///vf+uyzzzR48OAi8zMzM7VkyRJ169ZNVatWvaS9WdmpU6fUu3dvJSUl6aabbtKTTz6pKlWqaNeuXfrkk080b9487dmzRzVq1CjrVgGgzBDwAFzRdu7cqf79+6t27dpasWKFoqKinPNGjhyp7du368svvyzDDkvfoUOHFBYW5vby9erVU15env71r3+5BLysrCx99tln6tGjhz799FOXdXx9feXr6+utlp18fHwUGBjo9brnc8cdd6hixYpKSEgoNuAtWbJEGRkZGjRo0CXvrTzLy8tTQUHBOQP7+PHjlZSUpGnTpmnMmDEu8yZOnOj2/6QAACvjEE0AV7RXXnlFJ0+e1HvvvecS7gpdddVVGj16tPNxXl6epkyZonr16jkPDXvyySeVnZ3tsp7NZtOkSZOK1IuNjXXZA1d4btoPP/yg+Ph4hYeHq0KFCrrzzjt1+PBhl/V+++03rVq1ynkIZMeOHUvctoyMDI0bN041a9ZUQECAGjZsqFdffVXGGEn/O+dr5cqV+u2335x13TkXacCAAfr4449VUFDgHPv3v/+tzMxM9evXr8jyxZ2Dt27dOsXFxalatWoKCgpSnTp1dP/997us99FHH6lVq1aqWLGiQkND1bx5c82YMcM5v7jzpzp27KhmzZrp999/V6dOnRQcHKyYmBi98sorRfravXu37rjjDlWoUEEREREaO3asli5det7XISgoSL1799by5ct16NChIvMTEhJUsWJF3XHHHTp27Jgee+wxNW/eXCEhIQoNDVX37t31888/n7P+mdtS3O/5vvvuU2xsrMtYQUGBpk+frqZNmyowMFDVq1fXgw8+qLS0NJfl3HndixMbG6vbbrtN33zzjVq2bKnAwEA1adJEixcvLrJsenq6xowZ43zvXXXVVXr55Zdd3i+F779XX31V06dPd/5N/f7778U+/19//aW33npLN998c5FwJ53+nwiPPfaYy967jRs3qnv37goNDVVISIi6dOmi1atXu7Wtxe0pP/v3Ufj+++STTzR58mTFxMSoYsWKuuuuu+RwOJSdna0xY8YoIiJCISEhGjp0aLGfFaNGjVJiYqKaNWumgIAANW3aVElJSeftEwCKwx48AFe0f//736pbt67atWvn1vLDhw/XvHnzdNddd2ncuHFas2aNXnrpJW3evFmfffbZBffx6KOPqnLlypo4caJ27dql6dOna9SoUfr4448lSdOnT9ejjz6qkJAQPfXUU5Kk6tWrn7OeMUZ33HGHVq5cqWHDhqlly5ZaunSpxo8fr3379mnatGkKDw/XP//5T73wwgs6efKkXnrpJUlS48aNz9vvwIEDNWnSJH333Xfq3LmzpNOhpkuXLoqIiDjv+ocOHdItt9yi8PBw/d///Z/CwsK0a9cul7CwbNkyDRgwQF26dNHLL78sSdq8ebN++OEHl9BdnLS0NHXr1k29e/dWv379tGjRIj3++ONq3ry5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IiJCCxYsKLZO4R4yd173i1VQUKCbb75ZEyZMKHZ+YSAsFBQU5FbdRo0aSZJ+/fVXtWzZ8qJ6PJ9z/Y3n5+cX+9461/vN3fdhefz7B3D5IuABuKLddtttevvtt5WSkqK2bduWuGzt2rVVUFCgbdu2uVyIJDU1Venp6apdu7ZzrHLlykpPT3dZPycnRwcOHLjgXj0JlrVr19a3336rEydOuOxV27Jli3O+NwwcOFDDhw9XWFiYbr31Vo/Xv+GGG3TDDTfohRdeUEJCggYNGqSPPvpIw4cPl3T60Mrbb79dt99+uwoKCvTII4/orbfe0jPPPOPRnrbi1K5dW7///ruMMS6v7fbt2z2qM2jQID3zzDP65ZdflJCQoPr16+v66693zl+0aJE6deqk9957z2W99PR0VatWrcTalStXLvYwvbP3wNarV0/ffvut2rdv71ZgOt/rfi7bt28v8nr98ccfkuS8qme9evV08uRJ5x47b+nevbt8fX01f/78815oJTw8XMHBwdq6dWuReVu2bJGPj0+RvWtnKu7vVzr9up95yCcAXI44RBPAFW3ChAmqUKGChg8frtTU1CLz//zzT+dl+QsDzNlXAXzttdckST169HCO1atXr8i5Rm+//fY59+C5o0KFCsV+6SzOrbfeqvz8fM2cOdNlfNq0abLZbM4rSV6su+66SxMnTtTs2bM9utl4Wlpakb0ThXtlCg8XPHr0qMt8Hx8ftWjRwmWZixEXF6d9+/bp888/d45lZWXpnXfe8ahO4d66Z599Vj/99FORe9/5+voW2daFCxdq3759561dr149bdmyxeWWGT///LN++OEHl+X69eun/Px8TZkypUiNvLw85/vGnde9JPv373e5Wuzx48f14YcfqmXLloqMjHT2kpKSoqVLlxZZPz09vcj5Z+6qWbOmRowYoW+++UZvvPFGkfkFBQWaOnWq/vrrL/n6+uqWW27RkiVLXM6PTE1NVUJCgm688UbnIZ/FqVevnlavXq2cnBzn2BdffOHVwzoBoLSwBw/AFa1evXpKSEjQ3XffrcaNG2vw4MFq1qyZcnJylJycrIULFzrvh3X11VdryJAhevvtt5Wenq4OHTpo7dq1mjdvnnr16qVOnTo56w4fPlwPPfSQ+vTpo5tvvlk///yzli5det49NiVp1aqV3nzzTT3//PO66qqrFBER4bxFwdluv/12derUSU899ZR27dqlq6++Wt98842WLFmiMWPGuFzQ4WJUqlSp2Pv9nc+8efM0e/Zs3XnnnapXr55OnDihd955R6Ghoc4gPXz4cB07dkydO3dWjRo1tHv3br3xxhtq2bKlW7dyOJ8HH3xQM2fO1IABAzR69GhFRUVpwYIFzhunu7vHtE6dOmrXrp2WLFkiSUUC3m233abnnntOQ4cOVbt27fTrr79qwYIFbu0Juv/++/Xaa68pLi5Ow4YN06FDhzRnzhw1bdrU5SIhHTp00IMPPqiXXnpJP/30k2655RbZ7XZt27ZNCxcu1IwZM3TXXXe59bqXpEGDBho2bJh+/PFHVa9eXe+//75SU1M1d+5c5zLjx4/X559/rttuu0333XefWrVqpYyMDP36669atGiRdu3adcF/B1OnTtWff/6pv//971q8eLFuu+02Va5cWXv27NHChQu1ZcsW9e/fX5L0/PPPa9myZbrxxhv1yCOPyM/PT2+99Zays7OLvSfimYYPH65FixapW7du6tevn/7880/Nnz/fa383AFCqyuTanQBwmfnjjz/MiBEjTGxsrPH39zcVK1Y07du3N2+88YbJyspyLpebm2smT55s6tSpY+x2u6lZs6Z54oknXJYxxpj8/Hzz+OOPm2rVqpng4GATFxdntm/ffs7bJJx92friLt1+8OBB06NHD1OxYkUj6by3TDhx4oQZO3asiY6ONna73dSvX9/84x//cLkdgzEXfpuEc3HnNgkbNmwwAwYMMLVq1TIBAQEmIiLC3HbbbWbdunXOdRYtWmRuueUWExERYfz9/U2tWrXMgw8+aA4cOFDkuc6+TUJxPZ59awFjjNmxY4fp0aOHCQoKMuHh4WbcuHHm008/NZLM6tWr3XpNjDFm1qxZRpJp3bp1kXlZWVlm3LhxJioqygQFBZn27dublJSUIpfcL+42CcYYM3/+fFO3bl3j7+9vWrZsaZYuXVrsthhjzNtvv21atWplgoKCTMWKFU3z5s3NhAkTzP79+40x7r3u51K7dm3To0cPs3TpUtOiRQsTEBBgGjVq5PJ7LnTixAnzxBNPmKuuusr4+/ubatWqmXbt2plXX33VeTuBwu39xz/+cd7nPlNeXp559913zd/+9jdTqVIlY7fbTe3atc3QoUOL3EJhw4YNJi4uzoSEhJjg4GDTqVMnk5yc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XnpJPXr0KI0+AQAAAADn4fEevIyMDEVEREiSKleurMOHD0uSmjdvrg0bNni3OwAAAACA2zwOeA0bNtTWrVslSVdffbXeeust7du3T3PmzFFUVJTXGwQAAAAAuMfjQzRHjx6tAwcOSJImTpyobt26acGCBfL399cHH3zg7f4AAAAAAG5yO+DdddddGj58uAYNGiSbzSZJatWqlXbv3q0tW7aoVq1aqlatWqk1CgAAAAAomduHaKalpalHjx6qVauWnn32We3YsUOSFBwcrGuvvZZwBwAAAABlzO2At3z5cu3YsUPDhg3T/PnzVb9+fXXu3FkJCQnKzs4uzR4BAAAAAG7w6CIrtWvX1qRJk7Rjxw4tW7ZM0dHRGjFihKKiojRy5EitX7++tPoEAAAAAJyHx1fRLNS5c2fNnz9fBw8e1EsvvaSPPvpIbdq08WZvAAAAAAAPeHwVzTPt3LlTH3zwgT744AM5HA517drVW30BAAAAADzk8R68rKwszZ8/X507d1b9+vX14YcfatiwYdq5c6eSkpJKo0cAAAAAgBvc3oO3du1avf/++/r444+VlZWlO++8U0lJSerSpYvztgkAAAAAgLLjdsC74YYbdPXVV2vKlCkaNGiQKleuXJp9AQAAAAA85HbAW7duna699trS7AUAAAAAcBHcPgePcAcAAAAAl7cLvk0CAAAAAODyQsADAAAAAIsg4AEAAACARRDwAAAAAMAi3L6KZqFrrrmm2Pve2Ww2BQYG6qqrrtJ9992nTp06eaVBAAAAAIB7PN6D161bN+3YsUMVKlRQp06d1KlTJ4WEhOjPP//U9ddfrwMHDqhr165asmRJafQLAAAAADgHj/fgHTlyROPGjdMzzzzjMv78889r9+7d+uabbzRx4kRNmTJFPXv29FqjAAAAAICSebwH75NPPtGAAQOKjPfv31+ffPKJJGnAgAHaunXrxXcHAAAAAHCbxwEvMDBQycnJRcaTk5MVGBgoSSooKHD+DAAAAAC4NDw+RPPRRx/VQw89pPXr1+v666+XJP34449699139eSTT0qSli5dqpYtW3q1UQAAAABAyTwOeE8//bTq1KmjmTNn6p///KckqWHDhnrnnXc0cOBASdJDDz2khx9+2LudAgAAAABK5HHAk6RBgwZp0KBB55wfFBR0wQ0BAAAAAC7MBQU8ScrJydGhQ4dU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QvPnz1fNmjWVnJysBx54QL6+vho1alSpbQsAAAAAlAa3A1716tWVnJyshx9+WE888YSMMZJO3xMvLi5Os2bNUvXq1Uulyc2bNyspKUk//vijrrvuOknSG2+8oVtvvVWvvvqqoqOji6zjcDj03nvvKSEhQZ07d5YkzZ07V40bN9bq1at1ww036P7773dZp27dukpJSdHixYsJeAAAAADKHY9udF67dm199dVXSktL0/bt22WMUf369VW5cuXS6k+SlJKSorCwMGe4k6SuXbvKx8dHa9as0Z133llknfXr1ys3N1ddu3Z1jjVq1Ei1atVSSkqKbrjhhmKfy+FwqEqVKiX2k52drezsbOfjwnsD5ubmKjc316Nt87bC58/Ly3N5fOZYSfPcHaNG+emNGtSgBjWowWc9NahxpdUoS2Xdh80U7oq7jL344ouaN2+etm7d6jIeERGhyZMn6+GHHy6yTkJCgoYOHeoSxCSpdevW6tSpk15++eUi6yQnJ6tDhw768ssvdcstt5yzn0mTJmny5MnFPmdwcLC7mwUAAADAYjIzMzVw4EA5HI5i7yFe6kwZevzxx42kEqfNmzebF154wTRo0KDI+uHh4Wb27NnF1l6wYIHx9/cvMn799debCRMmFBn/9ddfTbVq1cyUKVPO23dWVpZxOBzOae/evUaSOXLkiMnJySnTKSMjwyQmJhqHw2ESExNNRkZGkbGS5rk7Ro3y0xs1qEENalCDz3pqUONKqVHW38VzcnLMkSNHjCTjcDjcSETe59Ehmt42btw43XfffSUuU7duXUVGRurQoUMu43l5eTp27JgiIyOLXS8yMlI5OTlKT09XWFiYczw1NbXIOr///ru6dOmiBx54QE8//fR5+w4ICFBAQECRcbvdXuK9Ai8lP7/Tv9oz+ykcK2meu2PUKD+9UYMa1KAGNfispwY1rpQal8N38bLuwa8snzw8PFzh4eHnXa5t27ZKT0/X+vXr1apVK0nSihUrVFBQoDZt2hS7TqtWrWS327V8+XL16dNHkrR161bt2bNHbdu2dS7322+/qXPnzhoyZIheeOEFL2wVAAAAAJQNt++DV5YaN26sbt26acSIEVq7dq1++OEHjRo1Sv3793deQXPfvn1q1KiR1q5dK0mqVKmShg0bpvj4eK1cuVLr16/X0KFD1bZtW+cFVjZt2qROnTrplltu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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2IAAAIjCAYAAABh3KjvAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABTL0lEQVR4nO3de3zO9f/H8ee12REzp23mNKecQ0TTARkjJSVFK2cdvhTmS+kkqXx1pIhUDn0jRUUHjeWUmNOQ5JByKgxh5jRme//+8N3162rDdenaZ/bZ43677fZ1vT/vz+d6fa7X1b573j7X5305jDFGAAAAAADL+OR3AQAAAABQ2BDEAAAAAMBiBDEAAAAAsBhBDAAAAAAsRhADAAAAAIsRxAAAAADAYgQxAAAAALAYQQwAAAAALEYQAwAAAACLEcQAAFfk/PnzGjZsmCpWrCgfHx916tTJ688xbdo0ORwO7d6926vHXbp0qRwOh5YuXerV4+aH3bt3y+FwaNq0afldCgDAAwQxAPgHfvvtNz388MOqWrWqAgMDFRISohtvvFHjxo3TmTNn8rs8SdI777yTJ3+kT5kyRa+++qruueceTZ8+XYMHD77o3JYtW8rhcKhGjRq5bk9MTJTD4ZDD4dCcOXO8XuvVomPHjgoODtaJEycuOicuLk7+/v46cuSIhZXZW1RUlPP95XA4VLRoUTVt2lQffvhhfpcGoBArkt8FAEBB9c0336hLly4KCAhQ9+7dVa9ePZ07d04//PCDhg4dqp9//lmTJ0/O7zL1zjvvqEyZMurZs6dXj7t48WKVL19eb775plvzAwMD9euvv2rNmjVq2rSpy7YZM2YoMDBQ6enpLuMPPvigunbtqoCAAK/VLUm33HKLzpw5I39/f68e93Li4uL01Vdf6YsvvlD37t1zbD99+rTmzZundu3aqXTp0pbWZncNGzbUkCFDJEkHDhzQ+++/rx49eujs2bPq169fPlcHoDAiiAHAFdi1a5e6du2qypUra/HixSpXrpxzW//+/fXrr7/qm2++yccK896hQ4cUGhrq9vxq1arp/Pnz+vjjj12CWHp6ur744gt16NBBn332mcs+vr6+8vX19VbJTj4+PgoMDPT6cS+nY8eOKl68uGbOnJlrEJs3b55OnTqluLg4y2sryM6fP6+srKxLBuvy5cvrgQcecD7u2bOnqlatqjfffJMgBiBf8NFEALgCr7zyik6ePKkPPvjAJYRlq169ugYOHOh8fP78eY0aNUrVqlVTQECAoqKi9NRTT+ns2bMu+zkcDj3//PM5jhcVFeVyRSv73qkVK1YoPj5eZcuWVdGiRXXXXXfp8OHDLvv9/PPPWrZsmfNjWS1btrzkuZ06dUpDhgxRxYoVFRAQoJo1a+q1116TMUbS/9+TtGTJEv3888/O47pzv1W3bt30ySefKCsryzn21Vdf6fTp07r33ntzzM/tHrF169YpNjZWZcqUUVBQkKpUqaLevXu77Ddr1iw1btxYxYsXV0hIiOrXr69x48Y5t+d2j1jLli1Vr149bdmyRa1atVJwcLDKly+vV155JUdde/bsUceOHVW0aFGFhYVp8ODBWrBgwWVfh6CgIN19991atGiRDh06lGP7zJkzVbx4cXXs2FFHjx7Vv//9b9WvX1/FihVTSEiI2rdvrx9//PGix//rueTW5549eyoqKsplLCsrS2PHjlXdunUVGBio8PBwPfzwwzp27JjLPHde99xERUXp9ttv18KFC9WwYUMFBgaqTp06+vzzz3PMTU1N1aBBg5zvverVq2vMmDEu75fs999rr72msWPHOv+b2rJly2Vr+auyZcuqVq1a+u2331zGL/f+l6S7775b1113nct+d9xxhxwOh7788kvn2OrVq+VwOPTtt996VBuAwoErYgBwBb766itVrVpVzZs3d2t+3759NX36dN1zzz0aMmSIVq9erdGjR2vr1q364osvrriOxx57TCVLltSIESO0e/dujR07VgMGDNAnn3wiSRo7dqwee+wxFStWTE8//bQkKTw8/KLHM8aoY8eOWrJkifr06aOGDRtqwYIFGjp0qPbt26c333xTZcuW1X//+1+99NJLOnnypEaPHi1Jql279mXrvf/++/X8889r6dKluvXWWyVdCB+tW7dWWFjYZfc/dOiQ2rZtq7Jly+rJJ59UaGiodu/e7fJHfWJiorp166bWrVtrzJgxkqStW7dqxYoVLuE4N8eOHVO7du109913695779WcOXP0xBNPqH79+mrfvr2kC3+o33rrrTpw4IAGDhyoiIgIzZw5U0uWLLls/dKFjydOnz5dn376qQYMGOAcP3r0qBYsWKBu3bopKChIP//8s+bOnasuXbqoSpUqOnjwoN599121aNFCW7Zs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/w033KAbbrhBL730kmbOnKm4uDjNmjVLffv2lXThI4V33HGH7rjjDmVlZelf//qX3n33XT377LMeXbnKTeXKlbVlyxYZY1xe219//dWj48TFxenZZ5/Vpk2bNHPmTNWoUUPXX3+9c/ucOXPUqlUrffDBBy77paamqkyZMpc8dsmSJV0+Tpnt71c0q1Wrpu+++0433nijW8Hmcq/7xfz66685Xq9ffvlFkpyrOFarVk0nT550hqW81qFDB7Vo0UIvv/yyHn74YRUtWtSj9//NN9+sc+fO6eOPP9a+ffucgeuWW25xBrFrrrnmkovjACjc+GgiAFyBYcOGqWjRourbt68OHjyYY/tvv/3mXC49O2j8fdW3N954Q9KFPwizVatWLce9MJMnT77oFTF3FC1aNEe4u5jbbrtNmZmZGj9+vMv4m2++KYfD4Vw58J+65557NGLECL3zzjsefanysWPHclzpadiwoSQ5PyZ35MgRl+0+Pj669tprXeb8E7Gxsdq3b5/LMuXp6el67733PDpO9tWv5557Ths3bszx3WG+vr45znX27Nnat2/fZY9drVo1bdu2zeWrDH788UetWLHCZd69996rzMxMjRo1Kscxzp8/73zfuPO6X8r+/ftdVgdNS0vThx9+qIYNGyoiIsJZS1JSkhYsWJBj/9TUVJ0/f/6yz+OpJ554QkeOHHH2zpP3f7NmzeTn56cxY8aoVKlSqlu3rqQLAW3VqlVatmwZV8MAXBJXxADgClSrVk0zZ87Ufffdp9q1a6t79+6qV6+ezp07p5UrV2r27NnO7/1q0KCBevToocmTJys1NVUtWrTQmjVrNH36dHXq1EmtWrVyHrdv37565JFH1LlzZ7Vp00Y//vijFixYcNkrIJfSuHFjTZw4US+++KKqV6+usLAw59Lxf3fHHXeoVatWevrpp7V79241aNBACxcu1Lx58zRo0CBVq1btiuv4qxIlSuT6fWmXM336dL3zzju66667VK1aNZ04cULvvfeeQkJCnIG3b9++Onr0qG699VZVqFBBe/bs0dtvv62GDRu6tcT+5Tz88MMaP368unXrpoEDB6pcuXKaMWOG8wui3b0CWaVKFTVv3lzz5s2TpBxB7Pbbb9cLL7ygXr16qXnz5vrpp580Y8YMVa1a9bLH7t27t9544w3FxsaqT58+OnTokCZNmqS6des6F5uRLtz79fDDD2v06NHauHGj2rZtKz8/P+3YsUOzZ8/WuHHjdM8997j1ul/KNddcoz59+mjt2rUKDw/XlClTdPDgQU2dOtU5Z+jQofryyy91++23q2fPnmrcuLFOnTqln376SXPmzNHu3bv/0X8HuWnfvr3q1aunN954Q/379/fo/R8cHKzGjRtr1apVzu8Qky5cETt16pROnTpFEANwafmzWCMA2MMvv/xi+vXrZ6Kiooy/v78pXry4ufHGG83bb79t0tPTnfMyMjLMyJEjTZUqVYyfn5+pWLGiGT58uMscY4zJzMw0TzzxhClTpowJDg42sbGx5tdff73o8vV/X048t2XZU1JSTIcOHUzx4sWNpMsuZX/ixAkzePBgExkZafz8/EyNGjXMq6++6rJMvjFXvnz9xbizfP369etNt27dTKVKlUxAQIAJCwszt99+u1m3bp1znzlz5pi2bduasLAw4+/vbypVqmQefvhhc+DAgRzP9ffl63Or8e9LvhtjzM6dO02HDh1MUFCQKVu2rBkyZIj57LPPjCSzatUqt14TY4yZMGGCkWSaNm2aY1t6eroZMmSIKVeunAkKCjI33nijSUpKyrE0fW7L1xtjzEcffWSqVq1q/P39TcOGDc2CBQtyPRdjjJk8ebJp3LixCQoKMsWLFzf169c3w4YNM/v37zfGuPe6X0zlypVNhw4dzIIFC8y1115rAgICTK1atVz6nO3EiRNm+PDhpnr16sbf39+UKVPGNG/e3Lz22mvm3LlzLuf76quvXva5/15DbqZNm+by+rn7/jfGmKFDhxpJZsyYMS7j1atXN5LMb7/95naNAAofhzFX8R3dAAAUEGPHjtXgwYP1xx9/qHz58vldzlUjKipK9erV09dff53fpQDAVYV7xAAA8NCZM2dcHqenp+vdd99VjRo1CGEAALdwjxgAAB66++67ValSJTVs2FDHjx/XRx99pG3btl10GXgAAP6OIAYAgIdiY2P1/vvva8aMGcrMzFSdOnU0a9Ys3XffffldGgCggOAeMQAAAACwGPeIAQAAAIDFCGIAAAAAYDHuEfOCrKws7d+/X8WLF3f7izwBAAAA2I8xRidOnFBkZKR8fC5+3Ysg5gX79+9XxYoV87sMAAAAAFeJ33//XRUqVLjodoKYFxQvXlzShRc7JCQkX2vJyMjQwoUL1bZtW/n5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S6F/nZ8dwnbs2KHvvvtOpUuXzpsTAAAAAID/8TiIjRkzRp988onz8b333qvSpUurfPny+vHHH71a3N/Fx8frvffe0/Tp07V161Y9+uijOnXqlHr16iVJ6t69u8tiHgMHDlRCQoJef/11bdu2Tc8//7zWrVunAQMGSLoQwu655x6tW7dOM2bMUGZmplJSUpSSkqJz587l6bkAAAAAKLw8DmKTJk1SxYoVJV24upSYmKhvv/1W7du319ChQ71e4F/dd999eu211/Tcc8+pYcOG2rhxoxISEpwLcuzdu1cHDhxwzm/evLlmzpypyZMnq0GDBpozZ47mzp2revXqSZL27dunL7/8Un/88YcaNmyocuXKOX9WrlyZp+cCAAAAoPDy+B6xlJQUZxD7+uuvde+996pt27aKiopSs2bNvF7g3w0YMMB5Revvli5dmmOsS5cu6tKlS67zo6KiZIzxZnkAAAAAcFkeXxErWbKkfv/9d0lSQkKCYmJiJEnGGGVmZnq3OgAAAACwIY+viN199926//77VaNGDR05ckTt27eXJG3YsEHVq1f3eoEAAAAAYDceB7E333xTUVFR+v333/XKK6+oWLFikqQDBw7oX//6l9cLBAAAAAC78TiI+fn56d///neO8cGDB3ulIAAAAACwuyv6HrH//ve/uummmxQZGak9e/ZIksaOHat58+Z5tTgAAAAAsCOPg9jEiRMVHx+v9u3bKzU11blAR2hoqMaOHevt+gAAAADAdjwOYm+//bbee+89Pf300/L19XWON2nSRD/99JNXiwMAAAAAO/I4iO3atUuNGjXKMR4QEKBTp055pSgAAAAAsDOPg1iVKlW0cePGHOMJCQmqXbu2N2oCAAAAAFvzeNXE+Ph49e/fX+np6TLGaM2aNfr44481evRovf/++3lRIwAAAADYisdBrG/fvgoKCtIzzzyj06dP6/7771dkZKTGjRunrl275kWNAAAAAGArHgcxSYqLi1NcXJxOnz6tkydPKiwszNt1AQAAAIBtXVEQyxYcHKzg4GBv1QIAAAAAhYLHQaxKlSpyOBwX3b5z585/VBAAAAAA2J3HQWzQoEEujzMyMrRhwwYlJCRo6NCh3qoLAAAAAGzL4yA2cODAXMcnTJigdevW/eOCAAAAAMDuPP4esYtp3769PvvsM28dDgAAAABsy2tBbM6cOSpV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AAAAANvyOIi9+eabuY4///zzOnny5D8uCAAAAADszmv3iD3wwAOaMmWKtw4HAAAAALbltSCWlJSkwMBAbx0OAAAAAGzL448m3n333S6PjTE6cOCA1q1bp2effdZrhQEAAACAXXkcxEqUKOHy2MfHRzVr1tQLL7ygtm3beq0wAAAAALArj4PY1KlT86IOAAAAACg0PA5i2ZKTk7V161ZJUt26ddWoUSOvFQUAAAAAduZxEDt06JC6du2qpUuXKjQ0VJKUmpqqVq1aadasWSpbtqy3awQAAAAAW/F41cTHHntMJ06c0M8//6yjR4/q6NGj2rx5s9LS0vT444/nRY0AAAAAYCseXxFLSEjQd999p9q1azvH6tSpowkTJrBYBwAAAAC4weMrYllZWfLz88sx7ufnp6ysLK8UBQAAAAB25nEQu/XWWzVw4EDt37/fObZv3z4NHjxYrVu39mpxAAAAAGBHHgex8ePHKy0tTVFRUapWrZqqVaumKlWqKC0tTW+//XZe1AgAAAAAtuLxPWIVK1bU+vXr9d1332nbtm2SpNq1aysmJsbrxQEAAACAHV3R94g5HA61adNGbdq08XY9AAAAAGB7bn80cfHixapTp47S0tJybDt+/Ljq1q2r5cuXe7U4AAAAALAjt4PY2LFj1a9fP4WEhOTYVqJECT388MN64403vFocAAAAANiR20Hsxx9/VLt27S66vW3btkpOTvZKUQAAAABgZ24HsYMHD+b6/WHZihQposOHD3ulKAAAAACwM7eDWPny5bV58+aLbt+0aZPKlSvnlaIAAAAAwM7cDmK33Xabnn32WaWnp+fYdubMGY0YMUK33367V4v7q6NHjyouLk4hISEKDQ1Vnz59dPLkyUvuk56erv79+6t06dIqVqyYOnfurIMHDzq3//jjj+rWrZsqVqyooKAg1a5dW+PGjcuzcwAAAAAAyYPl65955hl9/vnnuuaaazRgwADVrFlTkrRt2zZNmDBBmZmZevrpp/Os0Li4OB04cECJiYnKyMhQr1699NBDD2nmzJkX3Wfw4MH65ptvNHv2bJUoUUIDBgzQ3XffrRUrVkiSkpOTFRYWpo8++kgVK1bUypUr9dBDD8nX11cDBgzIs3MBAAAAULi5HcTCw8O1cuVKPfrooxo+fLiMMZIufKdYbGysJkyYoPDw8DwpcuvWrUpISNDa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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "No remaining missing values in the cleaned dataset.\n",
            "\n",
            "\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Split the Data using GroupShuffleSplit (taking \"Info_cluster\" grouping structure into consideration)"
      ],
      "metadata": {
        "id": "jRvUhC1U7-tC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Extract the 'Info_cluster' variable\n",
        "info_cluster = df['Info_cluster']\n",
        "\n",
        "# Initialize GroupShuffleSplit with the desired parameters\n",
        "group_splitter = GroupShuffleSplit(n_splits=1, train_size=0.75, random_state=50)\n",
        "\n",
        "# Split the dataset\n",
        "for train_index, eval_index in group_splitter.split(df, groups=info_cluster):\n",
        "    training_data = df.iloc[train_index]\n",
        "    evaluation_data = df.iloc[eval_index]\n",
        "\n",
        "\n",
        "# Calculate class balance in the original data\n",
        "class_balance_original = df['Class'].value_counts(normalize=True)\n",
        "\n",
        "# Calculate class balance in the training data\n",
        "class_balance_train = training_data['Class'].value_counts(normalize=True)\n",
        "\n",
        "# Calculate class balance in the evaluation data\n",
        "class_balance_eval = evaluation_data['Class'].value_counts(normalize=True)\n",
        "\n",
        "# Print the class balance\n",
        "print(\"Class balance in original data:\")\n",
        "print(class_balance_original)\n",
        "print(\"\\nClass balance in training data:\")\n",
        "print(class_balance_train)\n",
        "print(\"\\nClass balance in evaluation data:\")\n",
        "print(class_balance_eval)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l1VmkIPB5X9P",
        "outputId": "9cdbab26-b37e-44a1-8ff6-34e03c0eef03"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Class balance in original data:\n",
            "Class\n",
            "-1    0.985066\n",
            " 1    0.014934\n",
            "Name: proportion, dtype: float64\n",
            "\n",
            "Class balance in training data:\n",
            "Class\n",
            "-1    0.98591\n",
            " 1    0.01409\n",
            "Name: proportion, dtype: float64\n",
            "\n",
            "Class balance in evaluation data:\n",
            "Class\n",
            "-1    0.981768\n",
            " 1    0.018232\n",
            "Name: proportion, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Using Isolation Forest to identify outliers"
      ],
      "metadata": {
        "id": "6KsW-qwt8P8f"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Initialise Isolation Forest model (unspecified contamination)\n",
        "isolation_forest = IsolationForest(random_state=42)\n",
        "\n",
        "# Fit the model to the data and predict outliers\n",
        "outlier_preds = isolation_forest.fit_predict(training_data)\n",
        "\n",
        "# Identify outliers (outlier_preds == -1 indicates outliers)\n",
        "outliers = training_data[outlier_preds == -1]\n",
        "\n",
        "#--- this method identified [462 rows x 291 columns]\n",
        "\n",
        "# Initialize counters for outliers and inliers\n",
        "outlier_count = 0\n",
        "inlier_count = 0\n",
        "\n",
        "# Loop through the outlier predictions\n",
        "for pred in outlier_preds:\n",
        "    if pred == -1:\n",
        "        outlier_count += 1\n",
        "    elif pred == 1:\n",
        "        inlier_count += 1\n",
        "\n",
        "# Print the counts\n",
        "print(\"Number of Intial Outliers and Inliers using Isolation Forest\")\n",
        "print(\"Number of outliers (-1):\", outlier_count)\n",
        "print(\"Number of inliers (1):\", inlier_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d_leFDi46FbB",
        "outputId": "96825938-702e-4a04-95ab-98efb31036eb"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of Intial Outliers and Inliers using Isolation Forest\n",
            "Number of outliers (-1): 462\n",
            "Number of inliers (1): 9403\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Using Quantile capping on the Outliers identified"
      ],
      "metadata": {
        "id": "USSYyWpD8acu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Identify the rows that contain outliers based on the 'outliers' DataFrame\n",
        "outlier_indices = outliers[outliers == -1].index\n",
        "\n",
        "# Calculate the 5th and 95th percentiles for each column in the identified outlier rows\n",
        "outlier_data = training_data.loc[outlier_indices]\n",
        "percentiles_lower= outlier_data.quantile(0.05)\n",
        "percentiles_upper = outlier_data.quantile(0.95)\n",
        "\n",
        "# Apply quantile capping to the identified outlier rows\n",
        "for column in outliers.columns:\n",
        "    training_data.loc[outlier_indices, column] = training_data.loc[outlier_indices, column].clip(upper=percentiles_upper[column])"
      ],
      "metadata": {
        "id": "alNhqHfJ6FjT"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Retrying Isolation Forest after using Qunatile Capping"
      ],
      "metadata": {
        "id": "ycZj8lFy8hx9"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1r5wbBPtnx-A",
        "outputId": "4d63e294-e9a7-435e-b71c-455730066254"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "\n",
            "\n",
            "\n",
            "Number of detected Outliers and Inliners, using Isolation Forest, after Quantile Capping\n",
            "Number of outliers (-1): 445\n",
            "Number of inliers (1): 9420\n"
          ]
        }
      ],
      "source": [
        "# Initialise Isolation Forest model\n",
        "isolation_forest = IsolationForest(random_state=42)\n",
        "\n",
        "# Fit the model to the data and predict outliers\n",
        "outlier_preds = isolation_forest.fit_predict(training_data)\n",
        "\n",
        "# Identify outliers (outlier_preds == -1 indicates outliers)\n",
        "outliers = training_data[outlier_preds == -1]\n",
        "\n",
        "print(\"\\n\\n\\n\")\n",
        "### count inliers and outliers again\n",
        "outlier_count = 0\n",
        "inlier_count = 0\n",
        "for pred in outlier_preds:\n",
        "    if pred == -1:\n",
        "        outlier_count += 1\n",
        "    elif pred == 1:\n",
        "        inlier_count += 1\n",
        "print(\"Number of detected Outliers and Inliners, using Isolation Forest, after Quantile Capping\")\n",
        "print(\"Number of outliers (-1):\", outlier_count)\n",
        "print(\"Number of inliers (1):\", inlier_count)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Normalisation - scaling the data"
      ],
      "metadata": {
        "id": "KzoF6-UO8u1b"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PGjJ3u2-w3Xw",
        "outputId": "18ccb5ea-b510-465f-e16a-038c5426a833"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Minimum and Maximum values for each feature before scaling:\n",
            "     Info_cluster  Class  feat_esm1b_0  feat_esm1b_1  feat_esm1b_2  \\\n",
            "min             7     -1     -0.739531     -0.664717     -0.878746   \n",
            "max           283      1      0.784410      1.051745      0.974194   \n",
            "\n",
            "     feat_esm1b_3  feat_esm1b_4  feat_esm1b_5  feat_esm1b_6  feat_esm1b_7  \\\n",
            "min     -0.931084     -1.010501     -1.086608     -1.499195     -0.957883   \n",
            "max      0.824154      0.709081      0.838205      0.582508      1.052097   \n",
            "\n",
            "     ...  feat_esm1b_280  feat_esm1b_281  feat_esm1b_282  feat_esm1b_283  \\\n",
            "min  ...       -1.035132       -0.987730       -0.898706       -1.284584   \n",
            "max  ...        0.772923        0.966091        0.707259        0.908633   \n",
            "\n",
            "     feat_esm1b_284  feat_esm1b_285  feat_esm1b_286  feat_esm1b_287  \\\n",
            "min       -1.076593       -0.707514       -1.043452       -0.935589   \n",
            "max        0.707677        0.958485        0.898551        0.708880   \n",
            "\n",
            "     feat_esm1b_288  feat_esm1b_289  \n",
            "min       -0.860550       -1.059898  \n",
            "max        0.921726        0.992171  \n",
            "\n",
            "[2 rows x 291 columns]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-15-cf8c8647b952>:12: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  training_data[columns_to_scale] = scaler.fit_transform(training_data[columns_to_scale])\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Minimum and Maximum values for each feature after scaling:\n",
            "     Info_cluster  Class  feat_esm1b_0  feat_esm1b_1  feat_esm1b_2  \\\n",
            "min             7     -1           0.0           0.0           0.0   \n",
            "max           283      1           1.0           1.0           1.0   \n",
            "\n",
            "     feat_esm1b_3  feat_esm1b_4  feat_esm1b_5  feat_esm1b_6  feat_esm1b_7  \\\n",
            "min           0.0           0.0           0.0           0.0           0.0   \n",
            "max           1.0           1.0           1.0           1.0           1.0   \n",
            "\n",
            "     ...  feat_esm1b_280  feat_esm1b_281  feat_esm1b_282  feat_esm1b_283  \\\n",
            "min  ...             0.0             0.0             0.0             0.0   \n",
            "max  ...             1.0             1.0             1.0             1.0   \n",
            "\n",
            "     feat_esm1b_284  feat_esm1b_285  feat_esm1b_286  feat_esm1b_287  \\\n",
            "min             0.0             0.0             0.0             0.0   \n",
            "max             1.0             1.0             1.0             1.0   \n",
            "\n",
            "     feat_esm1b_288  feat_esm1b_289  \n",
            "min             0.0             0.0  \n",
            "max             1.0             1.0  \n",
            "\n",
            "[2 rows x 291 columns]\n",
            "\n",
            "Missing values in the 'Class' and 'Info_cluster' columns after scaling:\n",
            "Class           0\n",
            "Info_cluster    0\n",
            "dtype: int64\n"
          ]
        }
      ],
      "source": [
        "# Print the minimum and maximum values for each feature before scaling\n",
        "print(\"Minimum and Maximum values for each feature before scaling:\")\n",
        "print(training_data.agg(['min', 'max']))\n",
        "\n",
        "# Initialize MinMaxScaler\n",
        "scaler = MinMaxScaler()\n",
        "\n",
        "# Specify columns to scale (exclude 'Class' and 'Info_cluster')\n",
        "columns_to_scale = training_data.columns.drop(['Class', 'Info_cluster'])\n",
        "\n",
        "# Fit scaler to the selected columns and transform them\n",
        "training_data[columns_to_scale] = scaler.fit_transform(training_data[columns_to_scale])\n",
        "\n",
        "# Print the minimum and maximum values for each feature after scaling\n",
        "print(\"\\nMinimum and Maximum values for each feature after scaling:\")\n",
        "print(training_data.agg(['min', 'max']))\n",
        "\n",
        "# Check for missing values in the 'Class' and 'Info_cluster' columns after scaling\n",
        "missing_values_after_scaling = training_data[['Class', 'Info_cluster']].isnull().sum()\n",
        "print(\"\\nMissing values in the 'Class' and 'Info_cluster' columns after scaling:\")\n",
        "print(missing_values_after_scaling)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Feature Reduction - this step uses Information gain to Identify the top 10 features"
      ],
      "metadata": {
        "id": "-YsRt94f64e9"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 516
        },
        "id": "mOtvWz4_95zB",
        "outputId": "151c1bb9-1d36-4cdd-b62e-eb5926709340"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA6sAAAIjCAYAAADldo2EAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACO30lEQVR4nOzde1TVVf7/8dcBFEEOEAiCV1DRZJgU9auBJZgXsDIddXBMJxEDHTRHDS0aKzUTzbFkyvEyKl4r1HFGJxXTSbynZqJmSoEiVpLlBXRQUM75/eHy/DqBCohx0udjrbNWZ+999n5/PjTr+321PxeD2Ww2CwAAAAAAG2JX3QUAAAAAAPBzhFUAAAAAgM0hrAIAAAAAbA5hFQAAAABgcwirAAAAAACbQ1gFAAAAANgcwioAAAAAwOYQVgEAAAAANoewCgAAAACwOYRVAAAAAIDNIawCAO4pg8FQrk96evo9r2XOnDn6/e9/r0aNGslgMCg6OvqWYy9evKi4uDh5eXmpdu3a6ty5sz7//PNyrRMeHi6DwaCAgIAy+zdv3mw57tWrV1fmUO5ow4YNmjhxYrnHh4eHKygo6J7U8kv47rvvNHHiRGVkZNzztQoLCzVx4sRy/zubnp5+y3/v//CHP9yTGr/88ktNnDhROTk592R+APglOFR3AQCA+9uyZcusvi9dulSbN28u1d6yZct7Xsv06dN16dIltW/fXmfOnLnlOJPJpKeeekqHDh3SuHHjVKdOHf39739XeHi4Dhw4cMsQ+lO1atVSVlaW9u3bp/bt21v1rVixQrVq1dLVq1fv+phuZcOGDZo9e3aFAuuv2XfffadJkybJz89PrVu3vqdrFRYWatKkSZJuhPzyGjVqlP7v//7Pqs3Pz68KK/v/vvzyS02aNEnh4eH3bA0AuNcIqwCAe2rQoEFW3z/99FNt3ry5VPsvYdu2bZZdVRcXl1uOW716tXbv3q1Vq1apX79+kqSoqCg1b95cr7/+ut5///07rtW0aVNdv35dH3zwgVVYvXr1qv71r3/pqaee0j//+c+7P6gH3PXr12Uymaq7jHJ5/PHHLf8+/Vr973//U+3atau7DAAPCC4DBgBUu//973968cUX1bBhQzk6OqpFixb661//KrPZbDXOYDBo5MiRWrFihVq0aKFatWqpbdu22r59e7nWady4sQwGwx3HrV69WnXr1lWfPn0sbV5eXoqKitLatWtVVFRUrvUGDBig1NRUqzD1n//8R4WFhYqKiirzNwcPHlSPHj3k6uoqFxcXdenSRZ9++qnVmGvXrmnSpEkKCAhQrVq15Onpqccee0ybN2+WJEVHR2v27NmSrC/Drqib53vVqlUKDAyUk5OTQkJCdOTIEUnSvHnz1KxZM9WqVUvh4eGlLjm9eWnxgQMHFBoaKicnJ/n7+2vu3Lml1jp79qyGDh2qunXrqlatWmrVqpWWLFliNSYnJ0cGg0F//etfNWvWLDVt2lSOjo76+9//btmxHDJkiOV4Fy9eLEnasWOH5fJvR0dHNWzYUGPGjNGVK1es5o+OjpaLi4u+/fZb9e7dWy4uLvLy8lJCQoJKSkosNXh5eUmSJk2aZFmrKnaw9+7dq8jISLm5ucnZ2VlhYWHatWuX1ZhTp04pPj5eLVq0kJOTkzw9PfX73//e6twvXrxYv//97yVJnTt3LnWp/a3q9fPzs7o0fvHixTIYDNq2bZvi4+Pl7e2tBg0aWPo3btyoxx9/XLVr15bRaNRTTz2lo0ePWs2Zl5enIUOGqEGDBnJ0dJSvr6969erF5ckAyoWdVQBAtTKbzXrmmWe0detWDR06VK1bt9amTZs0btw4ffvtt3rnnXesxm/btk2pqakaNWqUJahERkZq3759VXbP5cGDB9WmTRvZ2Vn/N9327dtr/vz5+uqrr/Tb3/72jvM8++yzlnsbn3jiCUnS+++/ry5dusjb27vU+KNHj+rxxx+Xq6urxo8frxo1amjevHkKDw/Xtm3b1KFDB0nSxIkTlZSUpOeff17t27dXQUGBPvvsM33++efq1q2bhg0bpu+++67My60raseOHVq3bp1GjBghSUpKStLTTz+t8ePH6+9//7vi4+N14cIFvfXWW4qJidEnn3xi9fsLFy7oySefVFRUlAYMGKCVK1fqT3/6k2rWrKmYmBhJ0pUrVxQeHq6srCyNHDlS/v7+WrVqlaKjo3Xx4kX9+c9/tpozJSVFV69eVVxcnBwdHfW73/1Oly5d0muvvaa4uDg9/vjjkqTQ0FBJ0qpVq1RYWKg//elP8vT01L59+/Tuu+/qm2++0apVq6zmLikpUUREhDp06KC//vWv2rJli2bOnKmmTZvqT3/6k7y8vDRnzhz96U9/0u9+9zvLf9B45JFH7nguL126pB9//NGqzcPDQ3Z2dvrkk0/Uo0cPtW3bVq+//rrs7OyUkpKiJ554Qjt27LDszu/fv1+7d+/WH/7wBzVo0EA5OTmaM2eOwsPD9eWXX8rZ2VmdOnXSqFGj9Le//U2vvPKK5RL7yl5qHx8fLy8vL7322mv63//+J+nG5f2DBw9WRESEpk+frsLCQs2ZM0ePPfaYDh48aLn0uG/fvjp69KheeOEF+fn56ezZs9q8ebNyc3O5PBnAnZkBAPgFjRgxwvzT//Pz73//2yzJPGXKFKtx/fr1MxsMBnNWVpalTZJZkvmzzz6ztJ06dcpcq1Yt8+9+97sK1VG7dm3z4MGDb9kXExNTqn39+vVmSea0tLTbzh0WFmb+zW9+YzabzeZ27dqZhw4dajabzeYLFy6Ya9asaV6yZIl569atZknmVatWWX7Xu3dvc82aNc3Z2dmWtu+++85sNBrNnTp1srS1atXK/NRTT922hp+f5zv5ac03STI7OjqaT548aWmbN2+eWZLZx8fHXFBQYGlPTEw0S7IaGxYWZpZknjlzpqWtqKjI3Lp1a7O3t7e5uLjYbDabzbNmzTJLMi9fvtwyrri42BwSEmJ2cXGxrHPy5EmzJLOrq6v57NmzVrXu37/fLMmckpJS6tgKCwtLtSUlJZkNBoP51KlTlrbBgwebJZknT55sNTY4ONjctm1by/cffvjBLMn8+uuvl5q3LDf/1mV9Tp48aTaZTOaAgABzRESE2WQyWdXt7+9v7tat222PZc+ePWZJ5qVLl1raVq1aZZZk3rp1a6nxt6q9cePGVv+bSElJMUsyP/bYY+br169b2i9dumR2d3c3x8bGWv0+Ly/P7ObmZmm/cOGCWZJ5xowZdzxHAFAWLgMGAFSrDRs2yN7eXqNGjbJqf/HFF2U2m7Vx40ar9pCQELVt29byvVGjRurVq5c2bdpkuVTzbl25ckWOjo6l2mvVqmXpL69nn31Wa9asUXFxsVavXi17e3v97ne/KzWupKREH3/8sXr37q0mTZpY2n19ffXss89q586dKigokCS5u7vr6NGj+vrrryt6aBXWpUsXqx2wm7u7ffv2ldFoLNV+4sQJq987ODho2LBhlu81a9bUsGHDdPbsWR04cEDSjX8HfHx8NGDAAMu4GjVqaNSoUbp8+bK2bdtmNWffvn0tl+KWh5OTk+Wf//e//+nHH39UaGiozGazDh48WGr88OHDrb4//vjjpY6rMl577TVt3rzZ6uPj46OMjAx9/fXXevbZZ3Xu3Dn9+OOP+vHHH/W///1PXbp00fbt2y2Xkv/0WK5du6Zz586pWbNmcnd3L/fTqisqNjZW9vb2lu+bN2/WxYsXNWDAAEutP/74o+zt7dWhQwdt3brVUmvNmjWVnp6uCxcu3JPaANzfuAwYAFCtTp06pXr16lkFH+n/X7J46tQpq/aynsTbvHlzFRYW6ocffpCPj89d1+Tk5FTmfak3n97708BwJ3/4wx+UkJCgjRs3asWKFXr66adLHask/fDDDyosLFSLFi1K9bVs2VImk0mnT5/Wb37zG02ePFm9evVS8+bNFRQUpMjISP3xj38s16WoFdWoUSOr725ubpKkhg0bltn+81BSr169Ug/kad68uaQb938++uijOnXqlAICAkpddn2rfwf8/f0rdAy5ubl67bXXtG7dulL15efnW32vVatWqSD80EMPVUnY+u1vf6uuXbuWar/5Hx0GDx58y9/m5+froYce0pUrV5SUlKSUlBR9++23Vvd1//xYqsrPz/fNem9e2v5zrq6ukiRHR0dNnz5dL774ourWratHH31UTz/9tJ577rkq+d8pgPsfYRUAgJ/x9fUt89U2N9vq1atXobnCw8M1c+ZM7dq1q0qeANypUydlZ2dr7dq1+vjjj7VgwQK98847mjt3rp5//vm7nv+nfrqjVp52888einUvVOQ/FpSUlKhbt246f/68XnrpJT388MOqXbu2vv32W0VHR5d6kvCtjuteulnDjBkzbvnanZtPr37hhReUkpKi0aNHKyQkRG5ubpb3td7tU5FvdWXCz8/3zXWWLVtWZuh0cPj//+/l6NGj1bNnT/373//Wpk2b9OqrryopKUmffPKJgoOD76peAPc/wioAoFo1btxYW7Zs0aVLl6x2HI8fP27p/6myLn396quv5OzsXKFLQ2+ndevW2rFjh0wmk9Vu3969e+Xs7GzZGSyvZ599Vs8//7zc3d315JNPljnGy8tLzs7OyszMLNV3/Phx2dnZWe1menh4aMiQIRoyZIguX76sTp06aeLEiZawWpmn/94L3333XanXnXz11VeS/v87Rhs3bqzDhw+XOt+3+negLLc63iNHjuirr77SkiVL9Nxzz1nabz45uTKq+tw2bdpU0o0dybJ2Xn9q9erVGjx4sGbOnGlpu3r1qi5evFjuGh966KFS44uLi2/77uGy6vX29r5jvTfHv/jii3rxxRf19ddfq3Xr1po5c6aWL19ervUAPLi4ZxUAUK2efPJJlZSU6L333rNqf+edd2QwGNSjRw+r9j179ljdm3f69GmtXbtW3bt3r7JdsX79+un777/XmjVrLG0//vijVq1apZ49e5Z5P+ud5nv99df197//XTVr1ixzjL29vbp37661a9davdbj+++/1/vvv6/HHnvMcnnluXPnrH7r4uKiZs2aWV26fDMc/jyU/NKuX7+uefPmWb4XFxdr3rx58vLystx7/OSTTyovL0+pqalWv3v33Xfl4uKisLCwO65zq+O9+e/ET3d8zWazkpOTK31Mzs7OZa5VWW3btlXTpk3117/+VZcvXy7V/8MPP1j+2d7evtTu9bvvvltqV/R2f/+mTZuWet3T/Pnzy33Pd0REhFxdXTV16lRdu3btlvUWFhZaLp3/6dpGo7Hcr38C8GBjZxUAUK169uypzp076y9/+YtycnLUqlUrffzxx1q7dq1Gjx5t2cW5KSgoSBEREVavrpFuvPPyTv7zn//o0KFDkm48nObw4cOaMmWKJOmZZ56x3PPZr18/PfrooxoyZIi+/PJL1alTR3//+99VUlJSrnV+zs3NrVzv4ZwyZYo2b96sxx57TPHx8XJwcNC8efNUVFSkt956yzIuMDBQ4eHhatu2rTw8PPTZZ59p9erVGjlypGXMzSA4atQoRUREyN7eXn/4wx8qXPvdqlevnqZPn66cnBw1b95cqampysjI0Pz581WjRg1JUlxcnObNm6fo6GgdOHBAfn5+Wr16tXbt2qVZs2aVeY/vzzVt2lTu7u6aO3eujEajateurQ4dOujhhx9W06ZNlZCQoG+//Vaurq765z//eVf3oDo5OSkwMFCpqalq3ry5PDw8FBQUVOlXJ9nZ2WnBggXq0aOHfvOb32jIkCGqX7++vv32W23dulWurq76z3/+I0l6+umntWzZMrm5uSkwMFB79uzRli1b5OnpaTVn69atZW9vr+nTpys/P1+Ojo564okn5O3treeff17Dhw9X37591a1bNx06dEibNm1SnTp1ylWvq6ur5syZoz/+8Y9q06aN/vCHP8jLy0u5ublav369OnbsqPfee09fffWVunTpoqio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AAAAAGw6rLq5ucloNMre3l4+Pj4qKirS1KlTtWXLFoWEhEiSmjRpop07d2revHkKCwtTjRo1NGnSJMsc/v7+2rNnj1auXKmoqCi5uLjIyclJRUVF8vHxKVcdqampMplMWrBggSWApqSkyN3dXenp6WrXrp3y8/P19NNPq2nTppKkli1bWs1hMpm0aNEiGY1GBQYGqnPnzsrMzNSGDRtkZ2enFi1aaPr06dq6dWuFw+rIkSPVt29fSdKcOXOUlpamhQsXavz48RWaZ+HChXr22WetQuiJEye0c+dO1apVS//617/0448/Kj4+XufOnbOE/Z9LSkqy+hsAAAAAQEXZdFj9uaysLBUWFqpbt25W7cXFxQoODrZ8nz17thYtWqTc3FxduXJFxcXFat26daXXPXTokLKysmQ0Gq3ar169quzsbHXv3l3R0dGKiIhQt27d1LVrV0VFRcnX19cy1s/Pz+r3devWlb29vezs7Kzafvpgo/K6GdwlycHBQe3atdOxY8cqNMeePXt07NgxLVu2zKrdZDLJYDBoxYoVcnNzkyS9/fbb6tevn/7+97+XubuamJiosWPHWr4XFBSoYcOGFaoHAAAAwIPtVxVWL1++LElav3696tevb9Xn6OgoSfrwww+VkJCgmTNnKiQkREajUTNmzNDevXvvat22bdtqxYoVpfq8vLwk3dhpHTVqlNLS0pSamqoJEyZo8+bNlvtNa9SoYfU7g8FQZlt1PbhowYIFat26tdq2bWvV7uvrq/r161uCqnRj19hsNuubb75RQEBAqbkcHR0tfw8AAAAAqIxfVVgNDAyUo6OjcnNzFRYWVuaYXbt2KTQ0VPHx8Za27OxsqzE1a9ZUSUlJuddt06aNUlNT5e3tLVdX11uOCw4OVnBwsBITExUSEqL333//jg9HqgqffvqpOnXqJEm6fv26Dhw4oJEjR5b795cvX9bKlSuVlJRUqq9jx45atWqVLl++LBcXF0nSV199JTs7OzVo0KBqDgAAAAAAfsamnwb8c0ajUQkJCRozZoyWLFmi7Oxsff7553r33Xe1ZMkSSVJAQIA+++wzbdq0SV999ZVeffVV7d+/32oePz8/HT58WJmZmfrxxx917dq12647cOBA1alTR7169dKOHTt08uRJpaena9SoUfrmm2908uRJJSYmas+ePTp16pQ+/vhjff3116Xu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DNTChQtvmUe/fv3k7e3tnr5VfQAA3w/NKgAANtWxY0ePaYfDodra2iZvNyAg4Jb7q7tEtr55dWOYO3euNm3apGXLlunjjz+Wy+VS//79PZrA5vR93o+6m06dOHHCPc/b21u9e/dW79691aHD/99jsrCwUFOmTNGYMWP0/vvvq6ioSAsWLLhlHi1VHwDAt2hWAQBoJxISEnT69GmdPn3aPe/48eO6ePGi+vbt2+z7KygoUGZmph599FH1799fERERKi0t9Yjx8fHR9evXbznugoKCm7bdlDEnJiYqPj5eK1euvGUDuW/fPkVFRWnBggUaPHiwYmNjderUqTveNwCgefDoGgAA2om0tDT1799fU6ZM0csvv6yamhr98pe/1LBhwzR48OBm319sbKw2btyosWPHyuFwaNGiRTc1htHR0dqzZ49+8pOfyOl0qnPnzjdt57nnntPEiROVmJiotLQ0/f3vf9fGjRs97iz8fTkcDuXl5WnEiBEaOnSo5s+fr4SEBF27dk179uzR119/7b6ENzY2VmVlZcrPz9eQIUO0detWbdq06Y73DQBoHpxZBQCgnXA4HNq8ebM6deqkhx56SGlpaerZs6c2bNjQIvtbtWqVOnXqpJSUFI0dO1YjR47UD37wA4+YpUuXqrS0VL169ar3e7KSNH78eK1evVorV65Uv3799OqrryovL0+pqalNGt8Pf/hDHT58WH369NGsWbPUt29fpaSkaP369crJydEvfvELSdK4ceP0zDPP6KmnntLAgQO1b98+LVq0qEn7BgA0ncMYY6weBAAAAAAAN+LMKgAAAADAdmhWAQAAAAC2Q7MKAAAAALAdmlUAAAAAgO3QrAIAAAAAbIdmFQAAAABgOzSrAAAAAADboVkFAAAAANgOzSoAAAAAwHZoVgEAAAAAtkOzCgAAAACwnf8DL5sVn6ksRtUAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "# Define your feature matrix (X) and target variable (y)\n",
        "X = training_data.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y = training_data['Class']  # Target variable\n",
        "\n",
        "# Instantiate the SelectKBest feature selection method\n",
        "selector = SelectKBest(score_func=mutual_info_classif, k=10)  # Select top 10 features\n",
        "\n",
        "# Fit the selector to the data\n",
        "selector.fit(X, y)\n",
        "\n",
        "# Get the scores of the features\n",
        "scores = selector.scores_\n",
        "\n",
        "# Get the indices of the top 10 features\n",
        "top_indices = scores.argsort()[-10:][::-1]\n",
        "\n",
        "# Get the names of the top 10 features\n",
        "top_features = X.columns[top_indices]\n",
        "\n",
        "# Plot the scores of the top 10 features\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.barh(range(len(top_features)), scores[top_indices], align='center')\n",
        "plt.yticks(range(len(top_features)), top_features)\n",
        "plt.xlabel('Information Gain')\n",
        "plt.ylabel('Features')\n",
        "plt.title('Top 10 Most Important Features')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Use a Random Forest to identify the most important features - this is another way and is used here as a validation technique\n",
        "\n",
        "Most of the feature identifed by Information Gain and the random forest feature importance are similar. This suggest I have a good range of features for feature selection."
      ],
      "metadata": {
        "id": "xTuC5b8b--ny"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define features (X) and target variable (y) for training_subset\n",
        "X_train = training_data.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train = training_data['Class']  # Target variable\n",
        "\n",
        "# Initialize Random Forest Classifier\n",
        "random_forest = RandomForestClassifier(random_state=42)\n",
        "\n",
        "# Train the Random Forest Classifier\n",
        "random_forest.fit(X_train, y_train)\n",
        "\n",
        "# Get feature importances\n",
        "feature_importances = random_forest.feature_importances_\n",
        "\n",
        "# Create a DataFrame to store feature importances\n",
        "feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': feature_importances})\n",
        "\n",
        "# Sort features by importance and select top 15\n",
        "top_15_features = feature_importance_df.sort_values(by='Importance', ascending=False).head(15)\n",
        "\n",
        "# Visualize top 15 feature importances\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.barh(top_15_features['Feature'], top_15_features['Importance'])\n",
        "plt.xlabel('Importance')\n",
        "plt.ylabel('Feature')\n",
        "plt.title('Top 15 Feature Importances')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 516
        },
        "id": "25EFrxrU-6ep",
        "outputId": "92a1185f-d0cd-40ad-d5e2-2dcf41a8e2fd"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA6sAAAIjCAYAAADldo2EAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACy20lEQVR4nOzde1iVVf7//+cGFFE2MCgIHkFEg6EUZTKwES0VmjL8aIMfJz+JmOigmTpoUXawTDTTZMpRGQU1T6jjjE4qjE7iuTILtVISFLGSLE2QUFD2/v3Rz/1tBx44KFt9Pa5rX1d7rXWv9b7v7XXNvFnrXstgNpvNiIiIiIiIiNgQu/oOQEREREREROTXlKyKiIiIiIiIzVGyKiIiIiIiIjZHyaqIiIiIiIjYHCWrIiIiIiIiYnOUrIqIiIiIiIjNUbIqIiIiIiIiNkfJqoiIiIiIiNgcJasiIiIiIiJic5SsioiIiIiIiM1RsioiIjbNYDDc0CcrK+umxzJv3jz++Mc/0qZNGwwGAzExMVW2W7x48VXjLCwsvO44PXv2vOr1R44cqeO7+tnf/vY3Fi9efFP6rq2ePXsSFBRU32HU2Lfffsurr75KdnZ2fYciInJbcajvAERERK7lvffes/q+dOlStmzZUqk8ICDgpscyY8YMzp8/z/3338+pU6eu2/61117D19fXqszNze2GxmrVqhVJSUmVylu0aHFD11fX3/72N5o1a3bVBFxq7ttvv2XKlCn4+PjQuXPn+g5HROS2oWRVRERs2pAhQ6y+f/jhh2zZsqVS+a2wfft2y6yqs7Pzdds/8sgjhISE1GgsV1fXernHumQ2m7l48SJOTk71HUq9uHz5MiaTqb7DEBG5bWkZsIiI3PZ++ukn/vKXv9C6dWscHR3p2LEjb731Fmaz2aqdwWBgzJgxLF++nI4dO9KoUSO6du3Kjh07bmictm3bYjAYqhXb+fPnqaioqNY1N6KsrIxXXnmF9u3b4+joSOvWrZk0aRJlZWVW7dLS0njooYfw9PTE0dGRwMBA5s2bZ9XGx8eHL774gu3bt1uWG/fs2ROAV199tcp7vrLUOT8/36qfxx57jMzMTEJCQnBycmLBggUAnDt3jnHjxll+o/bt2zNjxowaJ3NXfss1a9YQGBiIk5MToaGhHDp0CIAFCxbQvn17GjVqRM+ePa3ihP+3tHj//v2EhYXh5OSEr68v8+fPrzTW6dOnGT58OM2bN6dRo0Z06tSJJUuWWLXJz8/HYDDw1ltvMWfOHPz8/HB0dORvf/sbv/vd7wAYNmyY5fleWXK9c+dOy9LyK7/j+PHjuXDhglX/MTExODs7880339C/f3+cnZ3x8PAgISGh0r8vk8lEcnIy9957L40aNcLDw4PIyEg++eQTq3bLli2ja9euODk54e7uzv/+7/9y8uRJqzZHjx5l4MCBeHl50ahRI1q1asX//u//UlRUdGM/lIhILWhmVUREbmtms5nHH3+cbdu2MXz4cDp37kxmZiYTJ07km2++4e2337Zqv337dtLT0xk7dqwlmYiMjOTjjz+u8/cie/XqRUlJCQ0bNiQiIoJZs2bh7+9/Q9dWVFTwww8/WJU1atQIZ2dnTCYTjz/+OLt27SIuLo6AgAAOHTrE22+/zVdffcW//vUvyzXz5s3jt7/9LY8//jgODg78+9//Jj4+HpPJxOjRowGYM2cOzzzzDM7Ozrz44osANG/evEb3nJOTw+DBgxk5ciQjRoygY8eOlJaWEh4ezjfffMPIkSNp06YNe/bsITExkVOnTjFnzpwajbVz5042bNhguY+kpCQee+wxJk2axN/+9jfi4+P58ccfefPNN4mNjeWDDz6wuv7HH3/kD3/4A9HR0QwePJjVq1fz5z//mYYNGxIbGwvAhQsX6NmzJ7m5uYwZMwZfX1/WrFlDTEwM586d49lnn7XqMy0tjYsXLxIXF4ejoyP/8z//w/nz53n55ZeJi4vj97//PQBhYWEArFmzhtLSUv785z/TtGlTPv74Y9555x2+/vpr1qxZY9V3RUUFERERdOvWjbfeeoutW7cya9Ys/Pz8+POf/2xpN3z4cBYvXswjjzzC008/zeXLl9m5cycffvihZab/jTfe4KWXXiI6Opqnn36a77//nnfeeYcePXrw2Wef4ebmRnl5OREREZSVlfHMM8/g5eXFN998w/vvv8+5c+dwdXWt0e8mInLDzCIiIreR0aNHm3/5P1//+te/zIB56tSpVu2eeOIJs8FgMOfm5lrKADNg/uSTTyxlJ06cMDdq1Mj8P//zP9WKo0mTJuahQ4dWWZeenm6OiYkxL1myxPzPf/7TPHnyZHPjxo3NzZo1MxcUFFy37/DwcEusv/xcGe+9994z29nZmXfu3Gl13fz5882Aeffu3Zay0tLSSv1HRESY27VrZ1X229/+1hweHl6p7SuvvGKu6v8upKWlmQHz8ePHLWVt27Y1A+aMjAyrtq+//rq5SZMm5q+++sqq/Pnnnzfb29tf95mEh4ebf/vb31qVAWZHR0er8RcsWGAGzF5eXubi4mJLeWJiYqVYrzzjWbNmWcrKysrMnTt3Nnt6eprLy8vNZrPZPGfOHDNgXrZsmaVdeXm5OTQ01Ozs7GwZ5/jx42bA7OLiYj59+rRVrPv27TMD5rS0tEr3VtXvk5SUZDYYDOYTJ05YyoYOHWoGzK+99ppV2+DgYHPXrl0t3z/44AMzYB47dmylfk0mk9lsNpvz8/PN9vb25jfeeMOq/tChQ2YHBwdL+WeffWYGzGvWrKnUl4jIraBlwCIiclvbtGkT9vb2jB071qr8L3/5C2azmc2bN1uVh4aG0rVrV8v3Nm3aEBUVRWZmZp0t142OjiYtLY2nnnqK/v378/rrr5OZmcmZM2d44403bqgPHx8ftmzZYvWZNGkS8PNsXEBAAPfccw8//PCD5fPQQw8BsG3bNks/v3xftKioiB9++IHw8HCOHTt2U5Zy+vr6EhERYVW2Zs0afv/73/Ob3/zGKt7evXtTUVFxw8uwf+3hhx/Gx8fH8r1bt24ADBw4EKPRWKn82LFjVtc7ODgwcuRIy/eGDRsycuRITp8+zf79+4Gf/315eXkxePBgS7sGDRowduxYSkpK2L59u1WfAwcOxMPD44bv4Ze/z08//cQPP/xAWFgYZrOZzz77rFL7UaNGWX3//e9/b3Vf//jHPzAYDLzyyiuVrr2ynHvdunWYTCaio6Otfg8vLy/8/f0t/36uzJxmZmZSWlp6w/ckIlJXtAxYRERuaydOnKBFixZWyQn8v92BT5w4YVVe1TLcDh06UFpayvfff4+Xl9dNifPBBx+kW7dubN269YbaN2nShN69e1dZd/ToUQ4fPnzVpOj06dOW/969ezevvPIKe/furZRwFBUV1flSzl/vfnwl3oMHD95QvNXRpk0bq+9X7qV169ZVlv/4449W5S1atKBJkyZWZR06dAB+fgf1gQce4MSJE/j7+2NnZ/33/av9+6rq/q+loKCAl19+mQ0bNlSK79d/TLjy/ukv/eY3v7G6Li8vjxYtWuDu7n7VMY8ePYrZbL7qkvQGDRpY7mXChAnMnj2b5cuX8/vf/57HH3+cIUOGaAmwiNwSSlZFRERukdatW5OTk1PrfkwmE/feey+zZ8++6jjwc+Ly8MMPc8899zB79mxat25Nw4YN2bRpE2+//fYNbW50tQ2lrjYLXdXOvyaTiT59+lhmhn/tSoJYXfb29tUqN/9qw62boTo7H1dUVNCnTx/Onj3Lc889xz333EOTJk345ptviImJqfT7XO2+qstkMmEwGNi8eXOVff5yp+tZs2YRExPD+vXr+c9//sPYsWNJSkriww8/pFWrVnUSj4jI1ShZFRGR21rbtm3ZunUr58+ft5pdPXLkiKX+l44ePVqpj6+++orGjRtXa/lmTRw7dqxOxvDz8+PAgQM8/PDD19yd+N///jdlZWVs2LDBahbyl8uEr7haP7/5zW+An3fz/eUZsb+eUbxevCUlJVedKa4v3377LT/99JPV7OpXX30FYFle3LZtWw4ePIjJZLKaXb3av6+qXO3ZHjp0iK+++oolS5bw1FNPWcq3bNlS7Xu5ws/Pj8zMTM6ePXvV2VU/Pz/MZjO+vr439IeCe++9l3vvvZfJkyezZ88eunfvzvz585k6dWqN4xQRuRF6Z1VERG5rf/jDH6ioqODdd9+1Kn/77bcxGAw88sgjVuV79+7l008/tXw/efIk69evp2/fvnU2c/X9999XKtu0aRP79+8nMjKy1v1HR0fzzTff8Pe//71S3YULF/jpp5+A/zcT98sZxaKiItLS0ipd16RJE86dO1ep3M/PD8DqvdKffvqp0tEt14t37969ZGZmVqo7d+4cly9fvuG+6tLly5ctR+sAlJeXs2DBAjw8PCzvNf/hD3+gsLCQ9PR0q+veeecdnJ2dCQ8Pv+44V5LhXz/fqn4fs9lMcnJyje9p4MCBmM1mpkyZUqnuyjgDBgzA3t6eKVOmVJptNpvNnDlzBoDi4uJKv829996LnZ1dpSOSRERuBs2siojIba1fv3706tWLF198kfz8fDp16sR//vMf1q9fz7hx4yzJ1hVBQUFERERYHV0DVPl/7n/t3//+NwcOHADg0qVLHDx40DK79Pjjj3PfffcBPx9LEhwcTEhICK6urnz66aekpqbSunVrXnjhhVrf8//93/+xevVqRo0axbZt2+jevTsVFRUcOXKE1atXW8457du3Lw0bNqRfv36MHDmSkpIS/v73v+Pp6cmpU6es+uzatSvz5s1j6tSptG/fHk9PTx566CH69u1LmzZtGD58OBMnTsTe3p7U1FQ8PDwoKCi4oXgnTpzIhg0beOyxx4iJiaFr16789NNPHDp0iLVr15Kfn0+zZs1q/Vyqq0WLFsyYMYP8/Hw6dOhAeno62dnZpKSkWN7bjIuLY8GCBcTExLB//358fHxYu3Ytu3fvZs6cOZXela6Kn58fbm5uzJ8/H6PRSJMmTejWrRv33HMPfn5+JCQk8M033+Di4sI//vGPSu+uVkevXr34v//7P/76179y9OhRIiMjMZlM7Ny5k169ejFmzBj8/PyYOnUqiYmJ5Ofn079/f4xGI8ePH+ef//wncXFxJCQk8MEHHzBmzBj++Mc/0qFDBy5fvsx7772Hvb09AwcOrHGMIiI3rH42IRYREamZXx9dYzabzefPnzePHz/e3KJFC3ODBg3M/v7+5pkzZ1qO6rgCMI8ePdq8bNkys7+/v9nR0dEcHBxs3rZt2w2NfeX4kKo+vzyW5MUXXzR37tzZ7Orqam7QoIG5TZs25j//+c/mwsLCGxqnqqNafq28vNw8Y8YM829/+1uzo6Oj+Te/+Y25a9eu5ilTppiLioos7TZs2GC+7777zI0aNTL7+PiYZ8yYYU5NTa10lEthYaH50UcfNRuNRjNgdYzN/v37zd26dTM3bNjQ3KZNG/Ps2bOvenTNo48+WmW858+fNycmJprbt29vbtiwoblZs2bmsLAw81tvvWU5JqY6z+PKb/lLV46PmTlzplX5tm3bKh3BcqXPTz75xBwaGmpu1KiRuW3btuZ333230vjfffedediwYeZmzZqZGzZsaL733nsrHUNztbGvWL9+vTkwMNDs4OBg9e/lyy+/NPfu3dvs7OxsbtasmXnEiBHmAwcOVPo3NXToUHOTJk0q9VvV0UKXL182z5w503zPPfeYGzZsaPbw8DA/8sgj5v3791u1+8c//mF+8MEHzU2aNDE3adLEfM8995hHjx5tzsnJMZvNZvOxY8fMsbGxZj8/P3OjRo3M7u7u5l69epm3bt1a5T2KiNQ1g9l8C3YbEBERsQEGg4HRo0dXWjIsd5+ePXvyww8/8Pnnn9d3KCIichV6Z1VERERERERsjpJVERERERERsTlKVkVERERERMTm6J1VERERERERsTmaWRURERERERGbo2RVREREREREbI5DfQcgdz6TycS3336L0WjEYDDUdzgiIiIiIlJPzGYz58+fp0WLFtjZXXvuVMmq3HTffvstrVu3ru8wRERERETERpw8eZJWrVpds42SVbnpjEYj8PM/SBcXl3qORkRERERE6ktxcTGtW7e25AjXomRVbrorS39dXFyUrIqIiIiIyA29HqgNlkRERERERMTmKFkVERERERERm6NkVURERERERGyOklURERERERGxOUpWRURERERExOYoWRURERERERGbo2RVREREREREbI6SVREREREREbE5SlZFRERERETE5ihZFREREREREZujZFVERERERERsjpJVERERERERsTlKVkVERERERMTmKFkVERERERERm6NkVURERERERGyOklURERERERGxOUpWRURERERExOYoWRURERERERGb41DfAcjdI+iVTOwcG9d3GCIicovkT3+0vkMQEZHbmGZWRURERERExOYoWRURERERERGbo2RVREREREREbI6SVREREREREbE5SlZFRERERETE5tRrsmo2m4mLi8Pd3R2DwUB2dnZ9hmNT8vPz9UxEREREROSuVa/JakZGBosXL+b999/n1KlTBAUF1brPmJgY+vfvX/vgbrKUlBR69uyJi4sLBoOBc+fO1fkYY8eOpWvXrjg6OtK5c+drts3NzcVoNOLm5mZVvm7dOkJCQnBzc6NJkyZ07tyZ9957r85jFRERERER+aV6TVbz8vLw9vYmLCwMLy8vHBzunmNfS0tLiYyM5IUXXrip48TGxjJo0KBrtrl06RKDBw/m97//faU6d3d3XnzxRfbu3cvBgwcZNmwYw4YNIzMz82aFLCIiIiIiUn/JakxMDM888wwFBQUYDAZ8fHwwmUwkJSXh6+uLk5MTnTp1Yu3atZZrKioqGD58uKW+Y8eOJCcnW+pfffVVlixZwvr16zEYDBgMBrKysq4by8mTJ4mOjsbNzQ13d3eioqLIz8+31GdlZXH//ffTpEkT3Nzc6N69OydOnLCM2blzZ1JTU2nTpg3Ozs7Ex8dTUVHBm2++iZeXF56enrzxxhtWY44bN47nn3+eBx544JqxHTlyhLCwMBo1akRQUBDbt2+/gaf7s7/+9a+MHj2adu3aXbPd5MmTueeee4iOjq5U17NnT/7nf/6HgIAA/Pz8ePbZZ7nvvvvYtWvXDcchIiIiIiJSXfU2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zJkzVrOsACNGjKBjx46EhITg4eHB7t27rzlm48aN2bFjB23atGHAgAEEBAQwfPhwLl68iIuLC40bN+bIkSMMHDiQDh06EBcXx+jRoxk5cmSt7nX+/PkEBwczYsQIAHr06EFwcDAbNmywajd9+nSmT59Op06d2LVrFxs2bKBZs2Y3PM6iRYsYMGAAbm5uleqcnZ3ZsmUL586dIyQkhCeffJJ+/frx17/+tVb3JiIiIiIici0Gs9lsru8g5M5WXFz88xE241Zj59i4vsMREZF6kj/90foOQURE6tmV3KCoqOiar1jCbTizKiIiIiIiInc+JavAtGnTcHZ2rvLzyCOP1Hd4NTZq1Kir3teoUaPqOzwREREREZGr0jJg4OzZs5U2LbrCycmp0jE5t4vTp09TXFxcZZ2Liwuenp63JA4tAxYREdAyYBERqd4y4Nvq6Jqbxd3dHXd39/oOo855enresoRURERERESkLilZlVvm8ykR1/3riYiIiIiICOidVREREREREbFBSlZFRERERETE5ihZFREREREREZujZFVERERERERsjjZYklsm6JVMHV0jIiLVpiNvRETuTppZFREREREREZujZFVERERERERsjpJVERERERERsTlKVkVERERERMTmKFkVERERERERm6NkVURERERERGxOvSarZrOZuLg43N3dMRgMZGdn12c4NiU/P1/PRERERERE7lr1mqxmZGSwePFi3n//fU6dOkVQUFCt+4yJiaF///61D+4mS0lJoWfPnri4uGAwGDh37lyd9n/gwAEGDx5M69atcXJyIiAggOTk5ErtsrKy6NKlC46OjrRv357Fixdftc/p06djMBgYN25cncYqIiIiIiLya/WarObl5eHt7U1YWBheXl44ODjUZzi3VGlpKZGRkbzwwgs3pf/9+/fj6enJsmXL+OKLL3jxxRdJTEzk3XfftbQ5fvw4jz76KL169SI7O5tx48bx9NNPk5mZWam/ffv2sWDBAu67776bEq+IiIiIiMgv1VuyGhMTwzPPPENBQQEGgwEfHx9MJhNJSUn4+vri5OREp06dWLt2reWaiooKhg8fbqnv2LGj1Wzhq6++ypIlS1i/fj0GgwGDwUBWVtZ1Yzl58iTR0dG4ubnh7u5OVFQU+fn5lvqsrCzuv/9+mjRpgpubG927d+fEiROWMTt37kxqaipt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iIiIiIiI3PmUrALTpk2zOgrnl59HHnmkvsOrsVGjRl31vq519IyIiIiIiEh90zJg4OzZs5U2LbrCycmp0jE5t4vTp09TXFxcZZ2Liwuenp63JA4tAxYRkbqgZcAiIre/6iwDvq2OrrlZ3N3dcXd3r+8w6pynp+ctS0hFRERERETqkpJVuWU+nxJx3b+eiIiIiIiIgN5ZFRERERERERukZFVERERERERsjpJVERERERERsTlKVkVERERERMTmKFkVERERERERm6PdgOWWCXolU+esiojIbUlnvIqI3HqaWRURERERERGbo2RVREREREREbI6SVREREREREbE5SlZFRERERETE5ihZFREREREREZtTr8mq2WwmLi4Od3d3DAYD2dnZ9RmOTcnPz9czERERERGRu1a9JqsZGRksXryY999/n1OnThEUFFTrPmNiYujfv3/tg7vJUlJS6NmzJy4uLhgMBs6dO1fnY4wdO5auXbvi6OhI586dK9VfSYh//fnwww+t2q1Zs4Z77rmHRo0ace+997Jp06Y6j1VEREREROSX6jVZzcvLw9vbm7CwMLy8vHBwuHuOfS0tLSUyMpIXXnjhpo4TGxvLoEGDrtlm69atnDp1yvLp2rWrpW7Pnj0MHjyY4cOH89lnn9G/f3/69+/P559/flPjFhERERGRu1u9JasxMTE888wzFBQUYDAY8PHxwWQykZSUhK+vL05OTnTq1Im1a9darqmoqGD48OGW+o4dO5KcnGypf/XVV1myZAnr16+3zBJmZWVdN5aTJ08SHR2Nm5sb7u7uREVFkZ+fb6nPysri/vvvp0mTJri5udG9e3dOnDhhGbNz586kpqbSpk0bnJ2diY+Pp6KigjfffBMvLy88PT154403rMYcN24czz//PA888MA1Yzty5AhhYWE0atSIoKAgtm/ffgNP92d//etfGT16NO3atbtmu6ZNm+Ll5WX5NGjQwFKXnJxMZGQkEydOJCAggNdff50uXbrw7rvv3nAcIiIiIiIi1VVvU5nJycn4+fmRkpLCvn37sLe3JykpiWXLljF//nz8/f3ZsWMHQ4YMwcPDg/DwcEwmE61atWLNmjU0bdqUPXv2EBcXh7e3N9HR0SQkJHD48GGKi4tJS0sDwN3d/ZpxXLp0iYiICEJDQ9m5cycODg5MnTqVyMhIDh48iJ2dHf3792fE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jbRp08ZqBnvu3Ln4+/sTEBDA22+/zY8//khsbOx1+//888956KGHiIiIYMKECRQWFgJgb29vmTFesWIFQ4cOJTk5mW7dulnaODk5Wf3+IiIiIiIidalayerQoUOBnzctCgsLu2aCd7O8/vrreHh4kJSUxLFjx3Bzc6NLly688MILAIwcOZLPPvuMQYMGYTAYGDx4MPHx8WzevNnSx4gRIywbI5WUlLBt2zZ69ux51TEbN27Mjh07eO655xgwYADnz5+nZcuWPPzww7i4uHDhwgWOHDnCkiVLOHPmDN7e3owePZqRI0fW6l7nz59v9Q7wldnTtLQ0YmJiLOXTp09n+vTpZGdn0759ezZs2ECzZs2u2//atWv5/vvvWbZsGcuWLbOUt23b1nIsT0pKCpcvX2b06NGMHj3a0mbo0KEsXry4VvcnIiIiIiJyNQaz2WyuTQcXL16kvLzcquxaS2Xl7lNcXIyrqyutx63GzrHx9S8QERGxYfnT9UqMiEhNXckNioqKrps31mg34NLSUsaMGYOnpydNmjThN7/5jdVHREREREREpDZqlKxOnDiRDz74gHnz5uHo6MjChQuZMmUKLVq0YOnSpXUd4003bdo0q6Nwfvl55JFH6ju8Ghs1atRV7+tmboQlIiIiIiJSWzVaBtymTRuWLl1Kz549cXFx4dNPP6V9+/a89957rFy5kk2bNt2MWG+as2fPcvbs2SrrnJycKh2Tc7s4ffo0xcXFVda5uLhc86zUuqRlwCIicifRMmARkZqrzjLgGp2zevbsWdq1awf8nPRcSfQefPBB/vznP9eky3rl7u5+U8+HrS+enp63LCEVERERERGpSzVKVtu1a8fx48dp06YN99xzD6tXr+b+++/n3//+N25ubnUcotwpPp8Soc23RERERETkhtTondVhw4Zx4MABAJ5//nnmzp1Lo0aNGD9+PBMnTqzTAEVEREREROTuU+ujawBOnDjB/v37ad++Pffdd19dxCV3kOqsSxcRERERkTvXTX9n9ZcuXrxI27Ztadu2bW27EhEREREREQFquAy4oqKC119/nZYtW+Ls7MyxY8cAeOmll1i0aFGdBigiIiIiIiJ3nxolq2+88QaLFy/mzTffpGHDhpbyoKAgFi5cWGfBiYiIiIiIyN2pRsuAly5dSkpKCg8//DCjRo2ylHfq1IkjR47UWXByZwl6JVPnrIqIyB1H566KiNwcNZpZ/eabb2jfvn2lcpPJxKVLl2odlIiIiIiIiNzdapSsBgYGsnPnzkrla9euJTg4uNZBiYiIiIiIyN2tRsuAX375ZYYOHco333yDyWRi3bp15OTksHTpUt5///26jlFERERERETuMtWaWT127Bhms5moqCj+/e9/s3XrVpo0acLLL7/M4cOH+fe//02fPn1uVqwiIiIiIiJyl6jWzKq/vz+nTp3C09OT3//+97i7u3Po0CGaN29+s+ITERERERGRu1C1ZlbNZrPV982bN/PTTz/VaUBVjRkXF4e7uzsGg4Hs7OybOt7tJD8/X89ERERERETuSDXaYOmKXyevN0NGRgaLFy/m/fff59SpUwQFBdW6z5iYGPr371/74G6ylJQUevbsiYuLCwaDgXPnztX5GP/9738JCwvDaDTi5eXFc889x+XLly31WVlZREVF4e3tTZMmTejcuTPLly+v8zhERERERER+qVrJqsFgwGAwVCq7mfLy8vD29iYsLAwvLy8cHGq0J9RtqbS0lMjISF544YWb0v+BAwf4wx/+QGRkJJ999hnp6els2LCB559/3tJmz5493HffffzjH//g4MGDDBs2jKeeekobaYmIiIiIyE1V7WXAMTExDBgwgAEDBnDx4kVGjRpl+X7lU1diYmJ45plnKCgowGAw4OPjg8lkIikpCV9fX5ycnOjUqRNr1661XFNRUcHw4cMt9R07diQ5OdlS/+qrr7JkyRLWr19vSb6zsrKuG8vJkyeJjo7Gzc0Nd3d3oqKiyM/Pt9RnZWVx//3306RJE9zc3OjevTsnTpywjNm5c2dSU1Np06YNzs7OxMfHU1FRwZtvvomXlxeenp688cYbVmOOGzeO559/ngceeOCasR05coSwsDAaNWpEUFAQ27dvv4GnC+np6dx33328/PLLtG/fnvDwcN58803mzp3L+fPnAXjhhRd4/fXXCQsLw8/Pj2effZbIyEjWrVt3Q2OIiIiIiIjURLWmKYcOHWr1fciQIXUazK8lJyfj5+dHSkoK+/btw97enqSkJJYtW8b8+fPx9/dnx44dDBkyBA8PD8LDwzGZTLRq1Yo1a9bQtGlT9uzZQ1xcHN7e3kRHR5OQkMDhw4cpLi4mLS0NAHd392vGcenSJSIiIggNDWXnzp04ODgwdepUIiMjOXjwIHZ2dvTv358RI0awcuVKysvL+fjjj61mnfPy8ti8eTMZGRnk5eXxxBNPcOzYMTp06MD27dvZs2cPsbGx9O7dm27dulXrOU2cOJE5c+YQGBjI7Nmz6devH8ePH6dp06bXvK6srIxGjRpZlTk5OXHx4kX2799Pz549q7yuqKiIgICAa/ZbVlZm+V5cXHzjNyMiIiIiIkI1k9Uryd2t4urqitFoxN7eHi8vL8rKypg2bRpbt24lNDQUgHbt2rFr1y4WLFhAeHg4DRo0YMqUKZY+fH192bt3L6tXryY6OhpnZ2ecnJwoKyvDy8vrhuJIT0/HZDKxcOFCSwKalpaGm5sbWVlZhISEUFRUxGOPPYafnx9ApWTOZDKRmpqK0WgkMDCQXr16kZOTw6ZNm7Czs6Njx47MmDGDbdu2VTtZHTNmDAMHDgRg3rx5ZGRksGjRIiZNmnTN6yIiIpgzZw4rV64kOjqawsJCXnvtNQBOnTpV5TWrV69m3759LFiw4Kr9JiUlWf0GIiIiIiIi1VWrDZZutdzcXEpLS+nTpw/Ozs6Wz9KlS8nLy7O0mzt3Ll27dsXDwwNnZ2dSUlIoKCio8bgHDhwgNzcXo9FoGdPd3Z2LFy+Sl5eHu7s7MTExRERE0K9fP5KTkyslez4+PhiNRsv35s2bExgYiJ2dnVXZ6dOnqx3flcQdwMHBgZCQEA4fPnzd6/r27cvMmTMZNWoUjo6OdOjQgT/84Q8AVnFdsW3bNoYNG8bf//53fvvb316138TERIqKiiyfkydPVvueRERERETk7nZb7VZUUlICwMaNG2nZsqVVnaOjIwCrVq0iISGBWbNmERoaitFoZObMmXz00Ue1Grdr165V7oLr4eEB/DzTOnbsWDIyMkhPT2fy5Mls2bLF8r5pgwYNrK4zGAxVlplMphrHWRMTJkxg/PjxnDp1it/85jfk5+eTmJhIu3btrNpt376dfv368fbbb/PUU09ds09HR0fL7yEiIiIiIlITt1WyGhgYiKOjIwUFBYSHh1fZZvfu3YSFhREfH28p++WsK0DDhg2pqKi44XG7dOlCeno6np6euLi4XLVdcHAwwcHBJCYmEhoayooVK667OVJd+PDDD+nRowcAly9fZv/+/YwZM+aGrzcYDLRo0QKAlStX0rp1a7p06WKpz8rK4rHHHmPGjBnExcXVbfAiIiIiIiJVuK2SVaPRSEJCAuPHj8dkMvHggw9SVFTE7t27cXFxYejQofj7+7N06VIyMzPx9fXlvffeY9++ffj6+lr68fHxITMzk5ycHJo2bYqrq2ulWc5fevLJJ5k5cyZRUVG89tprtGrVihMnTrBu3TomTZrEpUuXSElJ4fHHH6dFixbk5ORw9OjR685AXk9hYSGFhYXk5uYCcOjQIYxGI23atLHaFGru3Ln4+/sTEBDA22+/zY8//khsbOwNjTFz5kwiIyOxs7Nj3bp1TJ8+ndWrV2Nvbw/8vPT3scce49lnn2XgwIEUFhYCPyf819uYSkREREREpKZuq3dWAV5//XVeeuklkpKSCAgIIDIyko0bN1qS0ZEjRzJgwAAGDRpEt27dOHPmjNUsK8CIESPo2LEjISEheHh4sHv37muO2bhxY3bs2EGbNm0YMGAAAQEBDB8+nIsXL+Li4kLjxo05cuQIAwcOpEOHDsTFxTF69GhGjhxZq3udP38+wcHBjBgxAoAePXoQHBzMhg0brNpNnz6d6dOn06lTJ3bt2sWGDRto1qzZDY2xefNmfv/73xMSEsLGjRtZv349/fv3t9QvWbKE0tJSkpKS8Pb2tnzq8ogiERERERGRXzOYzWZzfQchd7bi4mJcXV1pPW41do6N6zscERGROpU//dH6DkFE5LZxJTcoKiq65iuWcBvOrIqIiIiIiMidT8kqMG3aNKujcH75eeSRR+o7vBobNWrUVe9r1KhR9R2eiIiIiIjIVWkZMHD27FnOnj1bZZ2Tk1OlY3JuF6dPn6a4uLjKOhcXFzw9PW9JHFoGLCIidzItAxYRuXHVWQZ8W+0GfLO4u7vfkTvbenp63rKEVEREREREpC4pWZVb5vMpEdf964mIiIiIiAjonVURERERERGxQUpWRURERERExOYoWRURERERERGbo2RVREREREREbI6SVREREREREbE52g1YbpmgVzJ1zqqIiMj/T+eziohcm2ZWRURERERExOYoWRURERERERGbo2RVREREREREbI6SVREREREREbE5SlZFRERERETE5ihZFREREREREZtTr8mq2WwmLi4Od3d3DAYD2dnZ9RmOTcnPz9czERERERGRu1a9JqsZGRksXryY999/n1OnThEUFFTrPmNiYujfv3/tg7vJUlJS6NmzJy4uLhgMBs6dO1en/R84cIDBgwfT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ETU0vSlWZTIZoqKiMG3aNGg0Grz66qsoLi5GWloa5HI5xowZAxcXF6xfvx579+6Fs7MzvvnmG2RkZMDZ2Vkcx8nJCXv37kVOTg6sra1hYWHx2Crno0aNGoUlS5YgKCgIH330Edq0aYPr169j+/btmDlzJioqKrB69WoMGTIEL7zwAnJycnDlyhW89dZb9ZpvYWEhCgsLkZubC+Cv+0JlMhkcHR21HoK0YsUKuLi4wM3NDZ999hlu376NsLCwJ45/4cIF/OMf/0BAQACmT5+OwsJCAIChoaG4YvzQ2rVr4e3tXeV7bqOjozFgwAA4OjqipKQEmzZtQmpqKvbu3Vuf6RMREREREdVIb4pVAJg/fz5sbW0RExODq1evwtLSEt27dxffRTp+/HicOXMGI0aMgEQiwciRIxEZGYk9e/aIY4SHh4sPRiotLcXBgwfRp0+fao/ZokULHD58GP/5z38wdOhQlJSUoHXr1ujXrx/kcjnu3buH7OxsJCQk4NatW3BwcMDEiRMxfvz4es115cqVWg8herh6Gh8fj9DQUHH7okWLsGjRImRmZqJjx45ITk6GjY3NE8fftm0bfv/9d2zYsAEbNmwQt7dr107rtTzFxcX49ttvtV4B9KibN2/irbfeQkFBASwsLPDyyy9j7969j91bTERERERE1JAkgiAIug6Cmje1Wg0LCwu0nboFBtIWug6HiIioWcpbNFDXIRARPdHD2qC4uLjG2zABwKDGViIiIiIiIiIdaPbF6sKFC2Fubl7lZ8CAAboO76lNmDCh2nlNmDBB1+ERERERERHVS7O/DLioqAhFRUVVtpmZmT32mpym4ubNm1Cr1VW2yeVyKBSKZxxR9XgZMBERUePjZcBE1BTU5TJgvXrAUmOwsrLSerpuc6FQKPSqICUiIiIiImpIzf4yYCIiIiIiImp6mv3KKumPC/MCnrjUT0REREREBHBllYiIiIiIiPQQi1UiIiIiIiLSOyxWiYiIiIiISO+wWCUiIiIiIiK9wwcs0TPTZc5evmeViIioCeG7W4lIl7iySkRERERERHqHxSoRERERERHpHRarREREREREpHdYrBIREREREZHeYbFKREREREREeofFKhEREREREekdnRargiAgIiICVlZWkEgkyMzM1GU4eiUvL4/nhIiIiIiInls6LVZTUlKwbt06/PDDDygoKECX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jY3NE8fftm0bfv/9d2zYsAEODg7i55VXXhH7mJubY9++fbhz5w68vLwwatQoDB48GF988YXYx8fHB5s2bcLq1avFVwl99913fMcqERERERE1KokgCIKug6DmTa1Ww8LCAm2nboGBtIWuwyEiIiKiBpC3aKCuQ6Am6GFtUFxcDLlcXmNfvVpZJSIiIiIiIgKeg2J14cKFMDc3r/IzYMAAXYf31CZMmFDtvCZMmKDr8IiIiIiIiOql2V8GXFRU9NhDix4yMzN77DU5TcXNmzehVqurbJPL5VAoFM84ourxMmAiIiKi5oeXAdPTqMtlwHrzntXGYmVlBSsrK12H0eAUCoVeFaREREREREQNqdkXq6Q/LswLeOJvT4iIiIiIiIDn4J5VIiIiIiIianpYrBIREREREZHeYbFKREREREREeofFKhEREREREekdFqtERERERESkd/g0YHpmuszZy/esEhERERE9Q035fbhcWSUiIiIiIiK9w2KViIiIiIiI9A6LVSIiIiIiItI7LFaJiIiIiIhI77BYJSIiIiIiIr3DYpWIiIiIiIj0jk6LVUEQEBERASsrK0gkEmRmZuoyHL2Sl5fHc0JERERERM8tnRarKSkpWLduHX744QcUFBSgS5cu9R4zNDQUwcHB9Q+uka1evRp9+vSBXC6HRCLBnTt3GvwYU6ZMgaenJ6RSKbp16/ZY+8OC+O+f48ePVzleYmIiJBJJkzi/RERERETUtBnp8uAqlQoODg7w8fHRZRg6cffuXQQGBiIwMBDR0dGNdpywsDCcOHEC586dq7bP/v378eKLL4rfra2tH+uTl5eHqKgovPbaa40SJxERERER0aN0trIaGhqKyZMnIz8/HxKJBE5OTtBoNIiJiYGzszPMzMzQtWtXbNu2TdynsrIS48aNE9tdXV0RGxsrts+dOxcJCQnYuXOnuEqYmpr6xFh+/vlnhISEwNLSElZWVggKCkJeXp7Ynpqaih49eqBly5awtLREr169cP36dfGY3bp1Q1xcHBwdHWFubo7IyEhUVlZi8eLFsLe3h0KhwIIFC7SOOXXqVLz33nvo2bNnjbFlZ2fDx8cHpqam6NKlCw4dOlSLs/uXL774AhMnTkT79u1r7GdtbQ17e3vxY2xsrNVeWVmJUaNGYd68eU8cCwDKysqgVqu1PkRERERERHWhs2I1NjYWH330Edq0aYOCggJkZGQgJiYG69evx8qVK3Hx4kVMmzYNb775pligaTQatGnTBlu3bsWlS5fw4Ycf4v3338eWLVsAAFFRUQgJCUFgYCAKCgpQUFDwxFXbiooKBAQEQCaT4ciRI0hLS4O5uTkCAwNRXl6OBw8eIDg4GL6+vjh37hzS09MREREBiUQijqFSqbBnzx6kpKRg8+bNWLt2LQYOHIhffvkFhw4dwieffIJZs2bhxIkTdT5PM2bMwLvvvoszZ85AqVRi8ODBuHXrVp3HqcmQIUOgUCjw6quvIjk5+bH2jz76CAqFAuPGjavVeDExMbCwsBA/bdu2bdB4iYiIiIio+dPZZcAWFhaQyWQwNDSEvb09ysrKsHDhQuzfvx9KpRIA0L59exw9ehSrVq2Cr68vjI2NMW/ePHEMZ2dnpKenY8uWLQgJCYG5uTnMzMxQVlYGe3v7WsWRlJQEjUaDNWvWiAVofHw8LC0tkZqaCi8vLxQXF2PQoEHo0KEDAMDNzU1rDI1Gg7i4OMhkMri7u6Nv377IycnB7t27YWBgAFdXV3zyySc4ePAgvL2963SeJk2ahGHDhgEAvvrqK6SkpGDt2rWYOXNmncapirm5OZYuXYpevXrBwMAA3377LYKDg/Hdd99hyJAhAICjR49i7dq1dXrQU3R0NKZPny5+V6vVLFiJiIiIiKhOdHrP6qNyc3Nx9+5d+Pv7a20vLy+Hh4eH+H3FihWIi4tDfn4+7t27h/Ly8iofHlRbZ8+eRW5uLmQymdb2+/fvQ6VSoX///ggNDUVAQAD8/f3h5+eHkJAQODg4iH2dnJy09rezs4OhoSEMDAy0tt28ebPO8T0s3AHAyMgIXl5eyMrKqvM4VbGxsdEqKl955RX89ttvWLJkCYYMGYKSkhKMHj0aX3/9NWxsbGo9rlQqhVQqbZAYiYiIiIjo+aQ3xWppaSkAYNeuXWjdurVW28PCJzExEVFRUVi6dCmUSiVkMhmWLFnyVJfXPnpcT09PbNy48bE2W1tbAH+ttE6ZMgUpKSlISkrCrFmzsG/fPvF+07/f4ymRSKrcptFonjrOZ8Xb2xv79u0D8NflzXl5eRg8eLDY/nAORkZGyMnJEVebiYiIiIiIGpLeFKvu7u6QSqXIz8+Hr69vlX3S0tLg4+ODyMhIcZtKpdLqY2JigsrKyloft3v37khKSoJCoYBcLq+2n4eHBzw8PBAdHQ2lUolNmzY98eFIDeH48ePo3bs3AODBgwc4ffo0Jk2a1GjHy8zMFFeNO3fujPPnz2u1z5o1CyUlJYiNjeWlvURERERE1Gj0pliVyWSIiorCtGnToNFo8Oqrr6K4uBhpaWmQy+UYM2YMXFxcsH79euzduxfOzs745ptvkJGRAWdnZ3EcJycn7N27Fzk5ObC2toaFhcVjq5yPGjVqFJYsWYKgoCDxgU/Xr1/H9u3bMXPmTFRUVGD16tUYMmQIXnjhBeTk5ODKlSt466236jXfwsJCFBYWIjc3FwBw/vx5yGQyODo6wsrKSuy3YsUKuLi4wM3NDZ999hlu376NsLCwWh0jNzcXpaWlKCwsxL1798T7Tt3d3WFiYoKEhASYmJiIl1lv374dcXFxWLNmDQCITyB+lKWlJQA0yDtxiYiIiIiIqqM3xSoAzJ8/H7a2toiJicHVq1dhaWmJ7t274/333wcAjB8/HmfOnMGIESMgkUgwcuRIREZGYs+ePeIY4eHh4oORSktLcfDgQfTp06faY7Zo0QKHDx/Gf/7zHwwdOhQlJSVo3bo1+vXrB7lcjnv37iE7OxsJCQm4desWHBwcMHHiRIwfP75ec125cqXWw6Ierp7Gx8cjNDRU3L5o0SIsWrQImZmZ6NixI5KTk2t9/+jbb7+t9aqbh0XptWvX4OTkBOCvc379+nUYGRmhc+fOSEpKwvDhw+s1NyIiIiIiovqSCIIg6DoIat7UavVfr7CZugUG0ha6DoeIiIiI6LmRt2igrkPQ8rA2KC4urvE2TECH71klIiIiIiIiqk6zL1YXLlwIc3PzKj8DBgzQdXhPbcKECdXOa8KECboOj4iIiIiIqF6a/WXARUVFKCoqqrLNzMzssdfkNBU3b96EWq2usk0ul0OhUDzjiKrHy4CJiIiIiHSjKV8GrFcPWGoMVlZWWk/XbS4UCoVeFaREREREREQNqdkXq6Q/LswLeOJvT4iIiIiIiIDn4J5VIiIiIiIianpYrBIREREREZHeYbFKREREREREeofFKhEREREREekdFqtERERERESkd1isEhERERERkd5hsUpERERERER6h8UqERERERER6R0Wq0RERERERKR3WKwSERERERGR3mGxSkRERERERHqHxSoRERERERHpHRarREREREREpHdYrBIREREREZHe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3d3F7+3atROCg4O1+ly7dk0AIJw5c6bGOVRWVgoymUz4/vvvxW0AhFmzZonfS0tLBQDCnj17BEEQhOjoaMHZ2VkoLy+vcswOHToImzZt0to2f/58QalU1hgLERHpBldWiYiImrmXX35Z/HdDQ0NYW1vjpZdeErfZ2dkBAG7evKm1n1KpFP/dysoKrq6uyMrKAgBkZWWhV69eWv179eqFK1euoLKyUtzm5eVVqxhv3LiB8PBwuLi4wMLCAnK5HKWlpcjPz692Li1btoRcLhfjzszMxGuvvQZjY+PHxv/zzz+hUqkwbtw4mJubi5+PP/5Y6zJhIiLSH0a6DoCIiIga19+LN4lEorVNIpEAADQaTYMfu2XLlrXqN2bMGNy6dQuxsbFo164dpFIplErlYw9lqmouD+M2MzOrdvzS0lIAwNdffw1vb2+tNkNDw1rFSEREzxaLVSIiIqrS8ePH4ejoCAC4ffs2Ll++DDc3NwCAm5sb0tLStPqnpaWhU6dONRZ/JiYmAKC1+vpw3y+//BKvv/46AODnn3/GH3/8Uad4X375ZSQkJKCiouKxotbOzg4vvPACrl69ilGjRtVpXCIi0g0Wq0RERFSljz76CNbW1rCzs8MHH3wAGxsb8f2t7777Ll555RXMnz8fI0aMQHp6Ov773/8+8em6CoUCZmZmSElJQZs2bWBqagoLCwu4uLjgm2++gZeXF9RqNWbMmFHjSmlVJk2ahOXLl+Pf//43oqOjYWFhgePHj6NHjx5wdXXFvHnzMGXKFFhYWCAwMBBlZWU4deoUbt++jenTpz/taSIiokbCe1aJiIioSosWLcI777wDT09PFBYW4vvvvxdXRrt3744tW7YgMTERXbp0wYcffoiPPvoIoaGhNY5pZGSEL774AqtWrcILL7yAoKAgAMDatWtx+/ZtdO/eHaNHj8aUKVOgUCjqFK+1tTUOHDiA0tJS+Pr6wtPTE19//bW4yvr2229jzZo1iI+Px0svvQRfX1+sW7dOfJ0OERHpF4kgCIKugyAiIiL9kZqair59++L27duwtLTUdThERPSc4soqERERERER6R0Wq0RERERERKR3eBkwERERERER6R2urBIREREREZHeYbFKREREREREeofFKhEREREREekdFqtERERERESkd1isEhERERERkd5hsUpERERERER6h8UqERERERER6R0Wq0RERERERKR3/h9giDwTc+pA8QAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Steps involved in Data Pre-processing\n",
        "\n",
        "1) Remove columns and rows that have majority missing values\n",
        "\n",
        "2) Split data into training and evaluation subsets (taking \"Info_cluster\" into consideration)\n",
        "\n",
        "3)Use Isolation forest to determine the outliers and then use quantile capping to cap at the 5th and 95th percentile\n",
        "\n",
        "4) Scale the training data using MinMaxScaler() and check the min-max range before and after scaling to ensure it worked\n",
        "\n",
        "5) preform feature reduction using Information gain to identify the top 10 most important features\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "6gLErTUZ8_-4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Preliminary Modelling**"
      ],
      "metadata": {
        "id": "tgN0tJG-7aBa"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Splitting the training data further into train_subset and eval_subset"
      ],
      "metadata": {
        "id": "cOP1a2Sd_fJO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Shuffle the unique values of Info_cluster\n",
        "unique_info_clusters = training_data['Info_cluster'].unique()\n",
        "np.random.shuffle(unique_info_clusters)\n",
        "\n",
        "# Split the unique values into training and evaluation clusters\n",
        "train_clusters, eval_clusters = train_test_split(unique_info_clusters, test_size=0.25, random_state=50)\n",
        "\n",
        "# Filter the training and evaluation subsets based on the selected clusters\n",
        "train_subset = training_data[training_data['Info_cluster'].isin(train_clusters)]\n",
        "eval_subset = training_data[training_data['Info_cluster'].isin(eval_clusters)]\n",
        "\n",
        "# Check the distribution of 'Info_cluster' values in each subset\n",
        "print(\"Training Subset Info_cluster Distribution:\")\n",
        "print(train_subset['Info_cluster'].value_counts())\n",
        "print(\"\\nEvaluation Subset Info_cluster Distribution:\")\n",
        "print(eval_subset['Info_cluster'].value_counts())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EKlpJ8ts7QQl",
        "outputId": "243ba3df-1697-45a5-836b-0aecf3b27e40"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training Subset Info_cluster Distribution:\n",
            "Info_cluster\n",
            "205    373\n",
            "153    206\n",
            "44     183\n",
            "168    142\n",
            "28     130\n",
            "      ... \n",
            "17       8\n",
            "118      6\n",
            "108      6\n",
            "227      5\n",
            "135      5\n",
            "Name: count, Length: 148, dtype: int64\n",
            "\n",
            "Evaluation Subset Info_cluster Distribution:\n",
            "Info_cluster\n",
            "154    305\n",
            "211    196\n",
            "142    170\n",
            "18     164\n",
            "132     95\n",
            "75      90\n",
            "119     86\n",
            "57      79\n",
            "125     78\n",
            "63      75\n",
            "13      73\n",
            "70      69\n",
            "62      67\n",
            "123     60\n",
            "187     54\n",
            "37      53\n",
            "60      50\n",
            "89      48\n",
            "229     48\n",
            "224     39\n",
            "122     37\n",
            "222     36\n",
            "215     36\n",
            "76      35\n",
            "73      35\n",
            "69      33\n",
            "91      33\n",
            "52      31\n",
            "199     30\n",
            "221     29\n",
            "274     27\n",
            "266     26\n",
            "275     25\n",
            "124     24\n",
            "228     24\n",
            "105     23\n",
            "130     22\n",
            "248     21\n",
            "66      17\n",
            "219     17\n",
            "49      15\n",
            "176     14\n",
            "206     13\n",
            "218     13\n",
            "45       9\n",
            "182      8\n",
            "19       7\n",
            "192      6\n",
            "159      4\n",
            "198      3\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Creating a preliminary Decision Tree to test performance (before class balancing)"
      ],
      "metadata": {
        "id": "9Y87dtLN_vgn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define X_train_subset with only the top 10 features\n",
        "X_train_subset = train_subset[top_features]\n",
        "\n",
        "# Define y_train_subset\n",
        "y_train_subset = train_subset['Class']\n",
        "\n",
        "# Instantiate the DecisionTreeClassifier\n",
        "decision_tree = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# Fit the decision tree to the training subset data\n",
        "decision_tree.fit(X_train_subset, y_train_subset)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "sGhZL8WM-xBE",
        "outputId": "3b173dcd-31b9-443a-bdd3-f419fbb0c071"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DecisionTreeClassifier(random_state=42)"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>DecisionTreeClassifier(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier(random_state=42)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "sing the eval-subset to check the performance of the preliminary model (before class balancing)"
      ],
      "metadata": {
        "id": "rJOJ94AaABv_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define X_eval_subset with only the top 10 features\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Predict the target values for the evaluation subset\n",
        "y_pred = decision_tree.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)\n",
        "\n",
        "#-- the incorrectly high accuracy, low precision, low recall and low F1-score suggests a class imbalance"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "INq3KAJR7QbR",
        "outputId": "9d2eb903-b066-47a6-d8cb-66fd405caf1f"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.9780564263322884\n",
            "Precision: 0.5321274133625677\n",
            "Recall: 0.5246460776526655\n",
            "F1-score: 0.5277821834522866\n",
            "Balanced Accuracy: 0.5246460776526655\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Decision Tree with Class Balancing**\n",
        "\n",
        "This part looks at Decision tree modelling after performing class balancing.\n",
        "\n",
        "It will help determine the best Class balancing technique to use.\n",
        "\n",
        "Using a Decision Tree with different class balancing techniques to find the best best one.\n",
        "\n",
        "SMOTE was chosen as it has best balanced performance between F1 and balanced accuracy. These metrics are less affected by class imbalance."
      ],
      "metadata": {
        "id": "wF5VSftuvVsl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Creating a Decison tree after class balancing using Under smapling.\n",
        "\n",
        "This can then be compared to the preliminary Decision tree to determine if there is any improvement in preformance."
      ],
      "metadata": {
        "id": "Bmxt9UKpwSNF"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rSWoOrU1kMzx",
        "outputId": "68567e21-0554-4000-bd13-666baed7b966"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.6986677115987461\n",
            "Precision: 0.5107365727678116\n",
            "Recall: 0.6732116992944914\n",
            "F1-score: 0.4374541181906809\n",
            "Balanced Accuracy: 0.6732116992944914\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Class\n",
              "-1    92\n",
              " 1    92\n",
              "Name: count, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ],
      "source": [
        "from imblearn.under_sampling import RandomUnderSampler\n",
        "\n",
        "# Initialize RandomUnderSampler\n",
        "undersampler = RandomUnderSampler(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset_us = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset_us = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform under-sampling\n",
        "X_resampled_us, y_resampled_us = undersampler.fit_resample(X_train_subset_us, y_train_subset_us)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "undersampled_df_us = pd.concat([pd.DataFrame(X_resampled_us, columns=X_train_subset_us.columns), pd.Series(y_resampled_us, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset\n",
        "undersampled_df_us = undersampled_df_us.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### Decision Tree using Undersampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the undersampled data\n",
        "X_train_subset_us = undersampled_df_us[top_features]\n",
        "\n",
        "# Define y_train_subset from the undersampled data\n",
        "y_train_subset_us = undersampled_df_us['Class']\n",
        "\n",
        "# Instantiate the DecisionTreeClassifier\n",
        "decision_tree_us = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# Fit the decision tree to the training subset data\n",
        "decision_tree_us.fit(X_train_subset_us, y_train_subset_us)\n",
        "\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval_us = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval_us = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the decision tree model\n",
        "y_pred_us = decision_tree_us.predict(X_eval_us)\n",
        "\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval_us, y_pred_us, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval_us, y_pred_us)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)\n",
        "\n",
        "# Count the number of samples in each class\n",
        "class_counts = undersampled_df_us['Class'].value_counts()\n",
        "\n",
        "class_counts"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Creating a Decison tree after class balancing using Over smapling.\n",
        "\n",
        "This can then be compared to the preliminary Decision tree to determine if there is any improvement in preformance."
      ],
      "metadata": {
        "id": "IOAoB_ZMBz9w"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v-5AN5c30JQN",
        "outputId": "af44c865-df38-4146-c732-f5b2c41b45a8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.9760971786833855\n",
            "Precision: 0.5259113766938363\n",
            "Recall: 0.5236532261832453\n",
            "F1-score: 0.5247164425175935\n",
            "Balanced Accuracy: 0.5236532261832453\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Class\n",
              "-1    7221\n",
              " 1    7221\n",
              "Name: count, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ],
      "source": [
        "from imblearn.over_sampling import RandomOverSampler\n",
        "# Initialize RandomOverSampler\n",
        "oversampler = RandomOverSampler(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset_os = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset_os = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform oversampling\n",
        "X_resampled_os, y_resampled_os = oversampler.fit_resample(X_train_subset_os, y_train_subset_os)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df_os = pd.concat([pd.DataFrame(X_resampled_os, columns=X_train_subset_os.columns), pd.Series(y_resampled_os, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset\n",
        "oversampled_df_os = oversampled_df_os.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### Decision Tree using Oversampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset_os = oversampled_df_os[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset_os = oversampled_df_os['Class']\n",
        "\n",
        "# Instantiate the DecisionTreeClassifier\n",
        "decision_tree_os = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# Fit the decision tree to the training subset data\n",
        "decision_tree_os.fit(X_train_subset_os, y_train_subset_os)\n",
        "\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval_os = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval_os = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the decision tree model\n",
        "y_pred_os = decision_tree_os.predict(X_eval_os)\n",
        "\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval_os, y_pred_os, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval_os, y_pred_os)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)\n",
        "\n",
        "# Count the number of samples in each class\n",
        "class_counts = oversampled_df_os['Class'].value_counts()\n",
        "\n",
        "class_counts"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Creating a Decison tree after class balancing using cost sensitive classification.\n",
        "\n",
        "This can then be compared to the preliminary Decision tree to determine if there is any improvement in preformance."
      ],
      "metadata": {
        "id": "I2NjXIWdB50h"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1JHs8zzkLQ3o",
        "outputId": "68b383b5-6a2c-468f-8906-1932f2423c41"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.9753134796238244\n",
            "Precision: 0.5239513034272859\n",
            "Recall: 0.5232560855954772\n",
            "F1-score: 0.5235970238148151\n",
            "Balanced Accuracy: 0.5232560855954772\n"
          ]
        }
      ],
      "source": [
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.metrics import classification_report\n",
        "from sklearn.utils.class_weight import compute_class_weight\n",
        "\n",
        "# Assume training_subset and eval_subset are already loaded\n",
        "# Assume top_features is a list containing the names of the top features\n",
        "\n",
        "# Separate features (X_train) and target variable (y_train) for training subset\n",
        "X_train = train_subset[top_features]\n",
        "y_train = train_subset['Class']\n",
        "\n",
        "# Compute class weights to handle class imbalance\n",
        "class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)\n",
        "\n",
        "# Initialize DecisionTreeClassifier with class weights\n",
        "# You can adjust other hyperparameters as needed\n",
        "decision_tree = DecisionTreeClassifier(class_weight=dict(zip(np.unique(y_train), class_weights)))\n",
        "\n",
        "# Fit the decision tree classifier to the training data\n",
        "decision_tree.fit(X_train, y_train)\n",
        "\n",
        "# Separate features (X_eval) and target variable (y_eval) for evaluation subset\n",
        "X_eval = eval_subset[top_features]\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Predict the target values for the evaluation subset\n",
        "y_pred = decision_tree.predict(X_eval)\n",
        "\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Creating a Decison tree after class balancing using SMOTE.\n",
        "\n",
        "This can then be compared to the preliminary Decision tree to determine if there is any improvement in preformance between different class balancing techniques."
      ],
      "metadata": {
        "id": "0WGKA_MECDb7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from imblearn.over_sampling import SMOTE\n",
        "\n",
        "# Initialize SMOTE\n",
        "smote = SMOTE(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform SMOTE over-sampling\n",
        "X_resampled, y_resampled = smote.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "########################### Decision Tree using Oversampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset = oversampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset = oversampled_df['Class']\n",
        "\n",
        "# Instantiate the DecisionTreeClassifier\n",
        "decision_tree = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# Fit the decision tree to the training subset data\n",
        "decision_tree.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the decision tree model\n",
        "y_pred = decision_tree.predict(X_eval)\n",
        "\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval_os, y_pred_os, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qdux9smMz3vw",
        "outputId": "db056bb9-89b0-45cb-f279-d0b53e1d2095"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.9760971786833855\n",
            "Precision: 0.5259113766938363\n",
            "Recall: 0.5236532261832453\n",
            "F1-score: 0.5247164425175935\n",
            "Balanced Accuracy: 0.53201653973742\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Random Forest Modelling**\n",
        "\n",
        "This section looks at modelling the Train susbset using a random forest with different class balancing\n",
        "balancing.\n",
        "\n",
        "This is done to try and improve the performance of the model.\n",
        "\n",
        "Random forest are resilent to class imbalance and are non-parametric models so have no presumption of the underlying data structure. This may lead to better performance compared to a decision tree.\n",
        "\n"
      ],
      "metadata": {
        "id": "d8vea0Vqwy3F"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wVBir0T4_dA0",
        "outputId": "3c911293-d6a9-4e95-f84e-f7033b8e0a16"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.8405172413793104\n",
            "Precision: 0.519611319266641\n",
            "Recall: 0.7015722095033406\n",
            "F1-score: 0.49901772816175527\n",
            "Balanced Accuracy: 0.7015722095033406\n"
          ]
        }
      ],
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from imblearn.under_sampling import RandomUnderSampler\n",
        "from sklearn.metrics import classification_report, balanced_accuracy_score\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize RandomUnderSampler\n",
        "undersampler = RandomUnderSampler(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform undersampling\n",
        "X_resampled, y_resampled = undersampler.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "undersampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "########################### New Random Forest using Undersampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the undersampled data\n",
        "X_train_subset = undersampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the undersampled data\n",
        "y_train_subset = undersampled_df['Class']\n",
        "\n",
        "# Instantiate the RandomForestClassifier\n",
        "random_forest = RandomForestClassifier(random_state=42)\n",
        "\n",
        "# Fit the random forest to the training subset data\n",
        "random_forest.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the random forest model\n",
        "y_pred = random_forest.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m1-yrA7IOLEE",
        "outputId": "c65fd9a0-ea2f-4639-b36b-067e3076bfc8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.6986677115987461\n",
            "Precision: 0.5107365727678116\n",
            "Recall: 0.6732116992944914\n",
            "F1-score: 0.4374541181906809\n",
            "Balanced Accuracy: 0.6732116992944914\n"
          ]
        }
      ],
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from imblearn.over_sampling import SMOTE\n",
        "from sklearn.metrics import classification_report\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize SMOTE\n",
        "smote = SMOTE(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform SMOTE over-sampling\n",
        "X_resampled, y_resampled = smote.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset (if necessary)\n",
        "# oversampled_df = oversampled_df.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### New Random Forest using Oversampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset = oversampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset = oversampled_df['Class']\n",
        "\n",
        "# Instantiate the RandomForestClassifier\n",
        "random_forest = RandomForestClassifier(random_state=42)\n",
        "\n",
        "# Fit the random forest to the training subset data\n",
        "random_forest.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the random forest model\n",
        "y_pred = random_forest.predict(X_eval)\n",
        "\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval_us, y_pred_us, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval_us, y_pred_us)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "IkSyt7w7VQHO"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Further Modelling**\n",
        "This Section looks at other modelling teachniques that can be used for Binary classificaiton.\n",
        "\n",
        "Models: Support Vector Machine (SVM), Logistic Regression and a Multilayer Perceptron (MLP).\n",
        "\n",
        "(Note: please change the Runtime to GPU - the use of a hardware accelerator allows for faster training of the Nueral Network)"
      ],
      "metadata": {
        "id": "v-Gt6z8B0Jcx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Support Vector Machine using SMOTE"
      ],
      "metadata": {
        "id": "qJt6WBkcA2bf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.svm import SVC\n",
        "from imblearn.over_sampling import SMOTE\n",
        "from sklearn.metrics import classification_report\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize SMOTE\n",
        "smote = SMOTE(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform SMOTE over-sampling\n",
        "X_resampled, y_resampled = smote.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset (if necessary)\n",
        "# oversampled_df = oversampled_df.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### New SVM using Oversampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset = oversampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset = oversampled_df['Class']\n",
        "\n",
        "# Instantiate the SVM classifier\n",
        "svm_classifier = SVC(random_state=42)\n",
        "\n",
        "# Fit the SVM classifier to the training subset data\n",
        "svm_classifier.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the SVM classifier\n",
        "y_pred = svm_classifier.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pGsJ0LOrstJy",
        "outputId": "ab31899c-ea03-4234-9609-829d01f35b51"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.8804858934169278\n",
            "Precision: 0.506325695137712\n",
            "Recall: 0.5477386347708265\n",
            "F1-score: 0.490073145245559\n",
            "Balanced Accuracy: 0.5477386347708265\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "MultiLayer Perception (Nueral Network) using SMOTE\n",
        "\n",
        "For better performance set GPU as Run time accelerator\n",
        "(In Google Colab - this can be done by clicking on: \"Runtime\" Tab, then \"change runtime type\" and selecting \"T4 GPU\""
      ],
      "metadata": {
        "id": "ShR9Og48BFQf"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wbk1lfWWDka0",
        "outputId": "5e8324d9-fd7a-4ea1-9047-0335b5d40574"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.6986677115987461\n",
            "Precision: 0.5107365727678116\n",
            "Recall: 0.6732116992944914\n",
            "F1-score: 0.4374541181906809\n",
            "Balanced Accuracy: 0.6732116992944914\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/neural_network/_multilayer_perceptron.py:693: UserWarning: Training interrupted by user.\n",
            "  warnings.warn(\"Training interrupted by user.\")\n"
          ]
        }
      ],
      "source": [
        "from imblearn.over_sampling import RandomOverSampler\n",
        "from sklearn.neural_network import MLPClassifier\n",
        "from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\n",
        "\n",
        "# Initialize RandomOverSampler\n",
        "oversampler = RandomOverSampler(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform oversampling\n",
        "X_resampled, y_resampled = oversampler.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset\n",
        "oversampled_df = oversampled_df.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### Neural Network using Oversampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset = oversampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset = oversampled_df['Class']\n",
        "\n",
        "# Instantiate the MLPClassifier (Neural Network)\n",
        "neural_network = MLPClassifier(hidden_layer_sizes=(100,),  # One hidden layer with 100 neurons\n",
        "                               activation='relu',  # Activation function\n",
        "                               solver='adam',  # Optimization algorithm\n",
        "                               alpha=0.0001,  # L2 regularization parameter\n",
        "                               batch_size='auto',  # Number of samples per batch\n",
        "                               learning_rate='constant',  # Learning rate schedule\n",
        "                               learning_rate_init=0.001,  # Initial learning rate\n",
        "                               max_iter=1000,  # Maximum number of iterations\n",
        "                               random_state=42)\n",
        "\n",
        "\n",
        "# Fit the neural network to the training subset data\n",
        "neural_network.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the neural network model\n",
        "y_pred = neural_network.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval_us, y_pred_us, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval_us, y_pred_us)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Logistic Regression using SMOTE"
      ],
      "metadata": {
        "id": "w7cpwoWAA_ni"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "from imblearn.over_sampling import SMOTE\n",
        "from sklearn.metrics import classification_report\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize SMOTE\n",
        "smote = SMOTE(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform SMOTE over-sampling\n",
        "X_resampled, y_resampled = smote.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset (if necessary)\n",
        "# oversampled_df = oversampled_df.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### Logistic Regression using Oversampled data ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset = oversampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset = oversampled_df['Class']\n",
        "\n",
        "# Instantiate the Logistic Regression classifier\n",
        "logistic_regression = LogisticRegression(random_state=42)\n",
        "\n",
        "# Fit the Logistic Regression classifier to the training subset data\n",
        "logistic_regression.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the Logistic Regression classifier\n",
        "y_pred = logistic_regression.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M45i4gtxs3eQ",
        "outputId": "8799d2e0-0ba4-49d6-de32-c31d54d0df4f"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores:\n",
            "Accuracy: 0.8303291536050157\n",
            "Precision: 0.5269209783958858\n",
            "Recall: 0.7979605662757557\n",
            "F1-score: 0.5067366301895131\n",
            "Balanced Accuracy: 0.7979605662757557\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Using SMOTE, Logistic Regression has the best balance Accuracy and F1 score from all the models."
      ],
      "metadata": {
        "id": "ZY-9suDtTveV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Modelling Summary - steps carried out**\n",
        "\n",
        "1) preliminary Modelling is preformed using a decison tree - this was before class balancing was preformed to test intial preformance\n",
        "\n",
        "2) Different class balancing techniques were used with a decision tree to identify the best class balance method for the data set. SMOTE was chosen as it was identifed as the best one - as it had the best score for F1 and balanced accuray metric. Undersampling was the second best.\n",
        "\n",
        "3) Random forest was then used with both undersampling and SMOTE. This was done to see if there was an improvement in performacne as Random forests are resistant to class imbalance.\n",
        "\n",
        "4) Support vector machine, Logistic Regression and a Neural Network were also trained to determine if these would lead to better performance. The F1 and balaced accuracy was compared across all models (after the dataset was treated with SMOTE). The Logistic Regression showed the best performance."
      ],
      "metadata": {
        "id": "xg6Y63YaCnit"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Hyperparameter Tuning**"
      ],
      "metadata": {
        "id": "Q0aQJo1cyXFK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Hyperparameter tuning of the Logistic Regression model - it had the best performance. Hyperparameter tuning was carried out in attempt to further improve the preformance the model."
      ],
      "metadata": {
        "id": "Ana3nsvxEvxn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "from imblearn.over_sampling import SMOTE\n",
        "from sklearn.metrics import classification_report, balanced_accuracy_score\n",
        "from sklearn.model_selection import GridSearchCV\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize SMOTE\n",
        "smote = SMOTE(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform SMOTE over-sampling\n",
        "X_resampled, y_resampled = smote.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the oversampled data\n",
        "X_train_subset = oversampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the oversampled data\n",
        "y_train_subset = oversampled_df['Class']\n",
        "\n",
        "# Define hyperparameters to tune\n",
        "param_grid = {\n",
        "    'C': [0.001, 0.01, 0.1, 1, 10, 100],  # Regularization parameter\n",
        "    'penalty': ['l2']  # Regularization type\n",
        "}\n",
        "\n",
        "# Instantiate the GridSearchCV object with logistic regression classifier and parameter grid\n",
        "grid_search = GridSearchCV(LogisticRegression(random_state=42, solver='lbfgs'), param_grid, cv=5, scoring='f1_macro')\n",
        "\n",
        "# Fit the grid search to the training data\n",
        "grid_search.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "# Get the best hyperparameters\n",
        "best_params = grid_search.best_params_\n",
        "\n",
        "# Instantiate logistic regression with the best hyperparameters\n",
        "logistic_regression_tuned = LogisticRegression(**best_params, random_state=42)\n",
        "\n",
        "# Fit the logistic regression classifier with the best hyperparameters to the training data\n",
        "logistic_regression_tuned.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the tuned Logistic Regression classifier\n",
        "y_pred_tuned = logistic_regression_tuned.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary for the tuned model\n",
        "report_dict_tuned = classification_report(y_eval, y_pred_tuned, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy for the tuned model\n",
        "balancedAccuracy_tuned = balanced_accuracy_score(y_eval, y_pred_tuned)\n",
        "\n",
        "# Print overall scores for the tuned model\n",
        "print(\"Overall Scores for Tuned Model:\")\n",
        "print(\"Accuracy:\", report_dict_tuned['accuracy'])\n",
        "print(\"Precision:\", report_dict_tuned['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict_tuned['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict_tuned['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy_tuned)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "REZOPUHBVmL-",
        "outputId": "43d24440-c0fa-4dea-af01-df96fa12703d"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overall Scores for Tuned Model:\n",
            "Accuracy: 0.8303291536050157\n",
            "Precision: 0.5269209783958858\n",
            "Recall: 0.7979605662757557\n",
            "F1-score: 0.5067366301895131\n",
            "Balanced Accuracy: 0.7979605662757557\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Hyperparameter tuning of the Random forest (after being treaed with Under sampling)"
      ],
      "metadata": {
        "id": "--91KCc5EugT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from imblearn.under_sampling import RandomUnderSampler\n",
        "from sklearn.model_selection import GridSearchCV\n",
        "from sklearn.metrics import classification_report\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize RandomUnderSampler without preserving class proportions\n",
        "undersampler = RandomUnderSampler(random_state=42, sampling_strategy='majority')\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform under-sampling\n",
        "X_resampled, y_resampled = undersampler.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "undersampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset (if necessary)\n",
        "# undersampled_df = undersampled_df.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### Random Forest with Hyperparameter Tuning ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the undersampled data\n",
        "X_train_subset = undersampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the undersampled data\n",
        "y_train_subset = undersampled_df['Class']\n",
        "\n",
        "# Define the parameter grid for hyperparameter tuning\n",
        "param_grid = {\n",
        "    'n_estimators': [50, 100, 200],\n",
        "    'max_depth': [None, 10, 20],\n",
        "    'min_samples_split': [2, 5, 10],\n",
        "    'min_samples_leaf': [1, 2, 4]\n",
        "}\n",
        "\n",
        "# Instantiate the RandomForestClassifier\n",
        "random_forest = RandomForestClassifier(random_state=42)\n",
        "\n",
        "# Initialize GridSearchCV with the classifier and parameter grid\n",
        "grid_search = GridSearchCV(random_forest, param_grid, cv=5, scoring='f1_macro')\n",
        "\n",
        "# Fit GridSearchCV to the training data\n",
        "grid_search.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "# Get the best hyperparameters\n",
        "best_params = grid_search.best_params_\n",
        "\n",
        "# Instantiate the RandomForestClassifier with the best hyperparameters\n",
        "best_random_forest = RandomForestClassifier(random_state=42, **best_params)\n",
        "\n",
        "# Fit the random forest to the training subset data\n",
        "best_random_forest.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the random forest model\n",
        "y_pred = best_random_forest.predict(X_eval)\n",
        "\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval_us, y_pred_us, output_dict=True)\n",
        "\n",
        "# Compute balanced accuracy\n",
        "balancedAccuracy = balanced_accuracy_score(y_eval_us, y_pred_us)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "print(\"Balanced Accuracy:\", balancedAccuracy)"
      ],
      "metadata": {
        "id": "Dq4--HgyCUM-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Hyperparameter tuning of the Decison Tree (after being treaed with Under sampling)"
      ],
      "metadata": {
        "id": "kLSWaou2FJkX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import GridSearchCV\n",
        "\n",
        "# Initialize RandomUnderSampler\n",
        "undersampler = RandomUnderSampler(random_state=42)\n",
        "\n",
        "# Define your feature matrix (X) and target variable (y) for training_subset\n",
        "X_train_subset = train_subset.drop(columns=['Class', 'Info_cluster'])  # Features\n",
        "y_train_subset = train_subset['Class']  # Target variable\n",
        "\n",
        "# Perform undersampling\n",
        "X_resampled, y_resampled = undersampler.fit_resample(X_train_subset, y_train_subset)\n",
        "\n",
        "# Convert back to DataFrame\n",
        "undersampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X_train_subset.columns), pd.Series(y_resampled, name='Class')], axis=1)\n",
        "\n",
        "# Shuffle the dataset\n",
        "undersampled_df = undersampled_df.sample(frac=1, random_state=42).reset_index(drop=True)\n",
        "\n",
        "########################### Decision Tree with Hyperparameter Tuning ##########################\n",
        "\n",
        "# Define X_train_subset with only the top 10 features from the undersampled data\n",
        "X_train_subset = undersampled_df[top_features]\n",
        "\n",
        "# Define y_train_subset from the undersampled data\n",
        "y_train_subset = undersampled_df['Class']\n",
        "\n",
        "# Define the parameter grid for hyperparameter tuning\n",
        "param_grid = {\n",
        "    'max_depth': [None, 5, 10, 20, 30, 50],  # Expanded range for max_depth\n",
        "}\n",
        "\n",
        "\n",
        "# Instantiate the DecisionTreeClassifier\n",
        "decision_tree = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# Initialize GridSearchCV with the classifier and parameter grid\n",
        "grid_search = GridSearchCV(decision_tree, param_grid, cv=5, scoring='f1_macro')\n",
        "\n",
        "# Fit GridSearchCV to the training data\n",
        "grid_search.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "# Get the best hyperparameters\n",
        "best_params = grid_search.best_params_\n",
        "\n",
        "# Instantiate the DecisionTreeClassifier with the best hyperparameters\n",
        "best_decision_tree = DecisionTreeClassifier(random_state=42, **best_params)\n",
        "\n",
        "# Fit the decision tree to the training subset data\n",
        "best_decision_tree.fit(X_train_subset, y_train_subset)\n",
        "\n",
        "################################## Checking performance using evaluation_training dataset #####################\n",
        "\n",
        "# Define X_eval with only the top 10 features from the evaluation_subset\n",
        "X_eval = eval_subset[top_features]\n",
        "\n",
        "# Define y_eval from the evaluation_subset\n",
        "y_eval = eval_subset['Class']\n",
        "\n",
        "# Make predictions on the evaluation data using the decision tree model\n",
        "y_pred = best_decision_tree.predict(X_eval)\n",
        "\n",
        "# Generate classification report as a dictionary\n",
        "report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "# Print overall scores\n",
        "print(\"Overall Scores:\")\n",
        "print(\"Accuracy:\", report_dict['accuracy'])\n",
        "print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "\n",
        "# Print best hyperparameters\n",
        "print(\"Best Hyperparameters:\", best_params)"
      ],
      "metadata": {
        "id": "7CsuUmNuydAx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Mining Pipeline**\n",
        "\n",
        "This Pipeline was created using Functional Programming"
      ],
      "metadata": {
        "id": "TslXlfMOnW5T"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "\n",
        "\n",
        "\n",
        "def drop_info_variables(df):\n",
        "    info_variables = ['Info_PepID','Info_organism_id', 'Info_protein_id', 'Info_pos', 'Info_AA', 'Info_epitope_id', 'Info_nPos', 'Info_nNeg']\n",
        "    return df.drop(info_variables, axis=1)\n",
        "\n",
        "def clean_missing_values(df, threshold_column=0.5, threshold_row=0.5):\n",
        "    missing_percentage_column = df.isnull().mean()\n",
        "    missing_percentage_row = df.isnull().mean(axis=1)\n",
        "\n",
        "    columns_to_drop = missing_percentage_column[missing_percentage_column > threshold_column].index.tolist()\n",
        "    rows_to_drop = missing_percentage_row[missing_percentage_row > threshold_row].index.tolist()\n",
        "\n",
        "    cleaned_df = df.drop(columns=columns_to_drop, index=rows_to_drop)\n",
        "\n",
        "    return cleaned_df\n",
        "\n",
        "\n",
        "from sklearn.ensemble import IsolationForest\n",
        "\n",
        "def quantile_capping(training_data, lower_quantile, upper_quantile):\n",
        "    # Initialise Isolation Forest model (unspecified contamination)\n",
        "    isolation_forest = IsolationForest(random_state=42)\n",
        "\n",
        "    # Fit the model to the data and predict outliers\n",
        "    outlier_preds = isolation_forest.fit_predict(training_data)\n",
        "\n",
        "    # Identify outliers (outlier_preds == -1 indicates outliers)\n",
        "    outliers = training_data[outlier_preds == -1]\n",
        "\n",
        "    # Identify the rows that contain outliers based on the 'outliers' DataFrame\n",
        "    outlier_indices = outliers.index\n",
        "\n",
        "    # Calculate the lower and upper percentiles for each column in the identified outlier rows\n",
        "    percentiles_lower = training_data.quantile(lower_quantile)\n",
        "    percentiles_upper = training_data.quantile(upper_quantile)\n",
        "\n",
        "    # Apply quantile capping to the identified outlier rows\n",
        "    for column in training_data.columns:\n",
        "        training_data.loc[outlier_indices, column] = training_data.loc[outlier_indices, column].clip(upper=percentiles_upper[column])\n",
        "\n",
        "    return training_data\n",
        "\n",
        "from sklearn.preprocessing import MinMaxScaler\n",
        "\n",
        "def scaling(training_data):\n",
        "    # Initialize MinMaxScaler\n",
        "    scaler = MinMaxScaler()\n",
        "\n",
        "    if 'Class' in training_data.columns:\n",
        "      # Specify columns to scale (exclude 'Class' and 'Info_cluster')\n",
        "      columns_to_scale = training_data.columns.drop(['Class', 'Info_cluster'])\n",
        "    else:\n",
        "      columns_to_scale = training_data.columns.drop(['Info_cluster'])\n",
        "\n",
        "    # Fit scaler to the selected columns and transform them\n",
        "    training_data[columns_to_scale] = scaler.fit_transform(training_data[columns_to_scale])\n",
        "\n",
        "    return training_data\n",
        "\n",
        "def select_top_features(X, y, k=10):\n",
        "    from sklearn.feature_selection import SelectKBest\n",
        "    from sklearn.feature_selection import mutual_info_classif\n",
        "\n",
        "    # Instantiate the SelectKBest feature selection method\n",
        "    selector = SelectKBest(score_func=mutual_info_classif, k=k)\n",
        "\n",
        "    # Fit the selector to the data\n",
        "    selector.fit(X, y)\n",
        "\n",
        "    # Get the scores\n",
        "    scores = selector.scores_\n",
        "\n",
        "    # Get the indices of the top k features\n",
        "    top_indices = scores.argsort()[-k:][::-1]\n",
        "\n",
        "    # Get the names of the top k features\n",
        "    top_features = X.columns[top_indices]\n",
        "\n",
        "    return top_features\n",
        "\n",
        "from imblearn.over_sampling import SMOTE\n",
        "\n",
        "def smote(X, y, random_state=42):\n",
        "    # Initialize SMOTE\n",
        "    smote = SMOTE(random_state=random_state)\n",
        "\n",
        "    # Perform SMOTE over-sampling\n",
        "    X_resampled, y_resampled = smote.fit_resample(X, y)\n",
        "\n",
        "    # Convert back to DataFrame\n",
        "    oversampled_df = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name=y.name)], axis=1)\n",
        "\n",
        "    return oversampled_df\n",
        "\n",
        "\n",
        "def logistic_regression(X, y, random_state=42):\n",
        "    # Instantiate the Logistic Regression classifier\n",
        "    logistic_regression = LogisticRegression(random_state=random_state)\n",
        "\n",
        "    # Fit the Logistic Regression classifier to the training subset data\n",
        "    logistic_regression.fit(X, y)\n",
        "\n",
        "    return logistic_regression\n",
        "\n",
        "from sklearn.metrics import classification_report, balanced_accuracy_score\n",
        "\n",
        "def evaluate_performance(logistic_regression, X_eval, y_eval):\n",
        "    # Make predictions on the evaluation data using the logistic regression classifier\n",
        "    y_pred = logistic_regression.predict(X_eval)\n",
        "\n",
        "    # Generate classification report as a dictionary\n",
        "    report_dict = classification_report(y_eval, y_pred, output_dict=True)\n",
        "\n",
        "    # Compute balanced accuracy\n",
        "    balanced_accuracy = balanced_accuracy_score(y_eval, y_pred)\n",
        "\n",
        "    # Print overall scores\n",
        "    print(\"Overall Scores:\")\n",
        "    print(\"Accuracy:\", report_dict['accuracy'])\n",
        "    print(\"Precision:\", report_dict['macro avg']['precision'])\n",
        "    print(\"Recall:\", report_dict['macro avg']['recall'])\n",
        "    print(\"F1-score:\", report_dict['macro avg']['f1-score'])\n",
        "    print(\"Balanced Accuracy:\", balanced_accuracy)\n",
        "\n",
        "    return\n",
        "\n",
        "\n",
        "\n",
        "path = \"df_reduced.csv\"\n",
        "df = pd.read_csv(path, sep=';')\n",
        "\n",
        "\n",
        "df = drop_info_variables(df)\n",
        "df = clean_missing_values(df)\n",
        "df = quantile_capping(df,0.05,0.95)\n",
        "df = scaling(df)\n",
        "\n",
        "# Split the dataset\n",
        "info_cluster = df['Info_cluster']\n",
        "group_splitter = GroupShuffleSplit(n_splits=1, train_size=0.75, random_state=50)\n",
        "for train_index, eval_index in group_splitter.split(df, groups=info_cluster):\n",
        "    training_data = df.iloc[train_index]\n",
        "    evaluation_data = df.iloc[eval_index]\n",
        "\n",
        "\n",
        "\n",
        "# Define X and y for training data\n",
        "train_X = training_data.drop(columns=['Class', 'Info_cluster'])\n",
        "train_y = training_data['Class']\n",
        "\n",
        "top_features = select_top_features(train_X,train_y)\n",
        "\n",
        "\n",
        "smote_train_data = smote(train_X,train_y)\n",
        "\n",
        "# updating the new class balanced X and y\n",
        "train_X = smote_train_data[top_features]\n",
        "train_y = smote_train_data['Class']\n",
        "\n",
        "\n",
        "\n",
        "logisticModel = logistic_regression(train_X, train_y)\n"
      ],
      "metadata": {
        "id": "RJDtSzLK9phM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "The performance metric of the Evaluation Dataset (split from the original dataset)"
      ],
      "metadata": {
        "id": "j7AqLaxBijXU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define X and y for evlauation data\n",
        "eval_X = evaluation_data[top_features]\n",
        "eval_y = evaluation_data['Class']\n",
        "\n",
        "\n",
        "evaluate_performance(logisticModel, eval_X, eval_y)\n"
      ],
      "metadata": {
        "id": "i_atLm_yiyeH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Using the Pipeline to predict the value for the reduced_holdout set"
      ],
      "metadata": {
        "id": "olp2ry2ikNKN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "path = \"df_reduced_holdout.csv\"\n",
        "df = pd.read_csv(path, sep=';')\n",
        "\n",
        "#processing the holdout_df\n",
        "holdout_df = drop_info_variables(df)\n",
        "holdout_df = clean_missing_values(holdout_df)\n",
        "holdout_df = quantile_capping(holdout_df,0.05,0.95)\n",
        "holdout_df = scaling(holdout_df)\n",
        "\n",
        "X = holdout_df[top_features]\n",
        "\n",
        "predicted_y = logisticModel.predict(X)\n",
        "\n",
        "# Add predicted values as a new column \"Class\"\n",
        "df['Class'] = predicted_y\n",
        "\n",
        "df.head()\n",
        "\n",
        "# Save the updated DataFrame as a CSV file with the same separator as the original file\n",
        "output_path = \"Iqbal_Usman_ CS4850_predictions.csv.\"\n",
        "df.to_csv(output_path, sep=';', index=False)\n",
        "\n",
        "# Print a message to confirm the save operation\n",
        "print(\"New file saved as:\", output_path)"
      ],
      "metadata": {
        "id": "O8HFkw0MkZ1O"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "WE-958D9XI9M",
        "eXhgxLKvTiRJ",
        "tgN0tJG-7aBa",
        "wF5VSftuvVsl",
        "d8vea0Vqwy3F",
        "v-Gt6z8B0Jcx",
        "Q0aQJo1cyXFK",
        "TslXlfMOnW5T"
      ]
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}