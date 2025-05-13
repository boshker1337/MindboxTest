from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Функция для получения пар продукт-категория
def get_product_category_pairs(products_df, categories_df, links_df):
    # Продукты с категориями
    products_with_cats = (
        products_df.join(links_df, "product_id")
        .join(categories_df, "category_id")
        .select("product_name", "category_name")
    )

    # Продукты без категорий
    products_without_cats = (
        products_df.join(links_df, "product_id", "left_anti")
        .select("product_name", lit(None).alias("category_name")
        )
    )
    
    # Объединяем результаты
    return  products_with_cats.union(products_without_cats)

# Создаем Spark сессию
spark = SparkSession.builder \
    .appName("ProductCategoryExample") \
    .getOrCreate()

# Подготовка тестовых данных
products_data = [
    (1, "Ноутбук"),
    (2, "Смартфон"), 
    (3, "Наушники"),
    (4, "Часы")  # У этого продукта нет категорий
]

categories_data = [
    (101, "Электроника"),
    (102, "Бытовая техника"), 
    (103, "Аксессуары")
]

links_data = [
    (1, 101),  # Ноутбук -> Электроника
    (2, 101),  # Смартфон -> Электроника
    (2, 103),  # Смартфон -> Аксессуары
    (3, 103)   # Наушники -> Аксессуары
]

# Создаем датафреймы
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
links_df = spark.createDataFrame(links_data, ["product_id", "category_id"])

# Получаем результат
result = get_product_category_pairs(products_df, categories_df, links_df)

# Выводим результат
result.orderBy("product_name").show()