# country-pca-kmeans-analysis
last UPD on Nov 6 2022

The initial data contains information on 10 indicators of 58 countries of the world community. Outliers have been identified and excluded. The number of principal components is 2 (to be able to plot them on a two-dimensional graph).<br>
This code uses the `sklearn` module for dimensionality reduction of the original data using the principal component method (PCA), as well as clustering using the K-means method. The user can specify the number of clusters and build graphs.
`QtDesigner` module is used for GUI. The interface supports two languages: English and Russian.<br>
The report contains information: on PCA — explained variance per component, its total percentage, as well as the eigenvalues of the vector;
on the K means method — The lowest SSE value (Sum of Squared Errors), cluster centers, the number of iterations required to converge clusters, as well as country counter.

# анализ-стран-методами-МГК-К_средних
Исходные данные содержат информацию о 10 показателях 58 стран мирового сообщества. Выбросы были выявлены и исключены. Количество главных компонент — 2 (чтобы было возможно изобразить их на двумерном графике).<br>
Данный код использует модуль `sklearn` для снижения размерности исходных данных методом главных компонент (МГК), а также кластеризации методом К средних.Пользователь может указать количество кластеров и построить графики.
GUI представлен модулем `QtDesigner`. Интерфейс поддерживает два языка: английский и русский.<br>
Отчёт содержит информацию: по методу главных компонент — долю объяснённой дисперсии на каждую компоненту, её общий процент, а также собственные значения вектора;
по методу К средних — наименьшее значение ошибки, координаты центров кластеров, число проведенных итераций для сходимости кластеров, а также распределение стран по кластерам.
