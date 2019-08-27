from typing import List

from django.core.exceptions import ValidationError

from ...product import AttributeInputType, models


def validate_attribute_input_for_product(instance: models.Attribute, values: List[str]):
    if not values:
        if not instance.value_required:
            return
        raise ValidationError(f"{instance.slug} expects a value but none were given")

    if instance.input_type != AttributeInputType.MULTISELECT and len(values) != 1:
        raise ValidationError(
            f"A {instance.input_type} attribute must take only one value"
        )

    for value in values:
        if not value.strip():
            raise ValidationError("Attribute values cannot be blank")


def validate_attribute_input_for_variant(instance: models.Attribute, values: List[str]):
    if not values:
        raise ValidationError(f"{instance.slug} expects a value but none were given")

    if len(values) != 1:
        raise ValidationError(f"A variant attribute cannot take more than one value")

    if not values[0].strip():
        raise ValidationError("Attribute values cannot be blank")
