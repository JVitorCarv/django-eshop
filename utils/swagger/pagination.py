from drf_yasg import openapi


def get_pagination_parameters() -> list[openapi.Parameter]:
    return [
        openapi.Parameter(
            name="page",
            in_=openapi.IN_QUERY,
            required=False,
            type=openapi.TYPE_INTEGER,
            description="Page number for paginated results",
        ),
        openapi.Parameter(
            name="res_per_page",
            in_=openapi.IN_QUERY,
            required=False,
            type=openapi.TYPE_INTEGER,
            description="Number of results per page",
        ),
    ]
