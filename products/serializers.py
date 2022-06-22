from rest_framework import serializers

from .models import ProductCategory as ProductCategoryModel
from .models import Product as ProductModel
from .models import ProductOption as ProductOptionModel


class ProductModelSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username'        
    # )

    class Meta:
        model = ProductModel
        fields = ["user", "title", "thumbnail", "detail_image", "product_categoy",
                  "description", "register_date", "exposure_start_date", "exposure_end_date"]


