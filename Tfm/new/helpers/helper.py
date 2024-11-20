import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import preprocessing
import matplotlib.pyplot as plt

# Converte lista de colunas para tipo de dados
# Exemplo:
# colunas = ['Column1','Column2','Column8']
# fn_convert_dtype(df, colunas, "int8")
def fn_convert_dtype(dataframe, columns, dtype):
    for column in columns:
        dataframe[column] = dataframe[column].astype(dtype)


# Valida o uso de memoria do dataset
# Exemplo:
# colunas = df.columns
# fn_memory_usage(df, colunas)
def fn_memory_usage(dataframe, columns) :
    stats_ram_usage = (
            (
                dataframe[columns]
                .memory_usage(deep=True)
                .sum()
            )
            /1e+6
        )

    print("Uso de Memória Ram: ", round(stats_ram_usage, 2), "MB" )


# Converte colunas categoricas em label encoder
# colunas = ["Column1","Column10","20"]
# fn_convert_label_encoder(df, colunas)
def fn_convert_label_encoder(dataframe, columns):
    label_encoder = preprocessing.LabelEncoder()
    for column in columns:
        dataframe[column]= label_encoder.fit_transform(dataframe[column])

# Converte colunas categoricas em one hot encoding
# Exemplo:
# colunas = ["Column1", "Column15"]
# df = fn_convert_one_hot_encoding(df, colunas)
def fn_convert_one_hot_encoding(dataframe, columns):
    for column in columns:    
        # Aplicando One-Hot Encoding usando get_dummies()
        dataframe=pd.concat([dataframe,pd.get_dummies(dataframe[column],prefix=column)],axis=1).drop([column],axis=1)

    return dataframe

# Retorna um relatorio de erros sobre a massa de dados teste e as predicoes
# Exemplo:
# fn_evaluate_model(y_test, y_pred)
def fn_evaluate_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)

    print("Accuracy: {:.2f}".format(accuracy))
    print("Precision: {:.2f}".format(precision))
    print("Recall: {:.2f}".format(recall))
    print("F1-score: {:.2f}".format(f1))
    print("Confusion Matrix:")
    print(confusion)


# Retorna um grafico de Matrix de confusao
# Exemplo:
# fn_confusion_matrix(y_test, y_pred_best_randomForestGrid, grid_search.classes_)
def fn_confusion_matrix(y_test, y_pred, classifier_classes):
    cm = confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=classifier_classes)

    disp.plot()
    plt.show()