from django_filters import (
    CharFilter,
    ChoiceFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
    NumberFilter,
)
from drf_yasg import openapi


def get_parameter_type(field: any) -> any:
    if isinstance(field, (CharFilter, ChoiceFilter, ModelChoiceFilter)):
        return openapi.TYPE_STRING
    elif isinstance(field, (ModelMultipleChoiceFilter)):
        return openapi.TYPE_ARRAY
    elif isinstance(field, (NumberFilter)):
        return openapi.TYPE_INTEGER
    else:
        return openapi.TYPE_STRING


def get_filter_parameters(filter_class) -> list[openapi.Parameter]:
    parameters = []
    for field_name, field in filter_class.base_filters.items():
        parameter = openapi.Parameter(
            name=field_name,
            in_=openapi.IN_QUERY,
            required=field.extra.get("required", False),
            type=get_parameter_type(field),
        )
        parameters.append(parameter)
    return parameters
