import reflex as rx
from app.components.layout import main_layout
from app.states.analytics_state import AnalyticsState


def metric_card(metric: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(metric["label"], class_name="text-sm font-medium text-gray-500"),
            rx.icon(metric["icon"], class_name="h-4 w-4 text-gray-400"),
            class_name="flex items-center justify-between pb-2",
        ),
        rx.el.p(metric["value"], class_name="text-2xl font-bold"),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
    )


def analytics_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Analytics",
                class_name="text-3xl font-bold tracking-tight text-gray-900",
            ),
            rx.el.div(
                rx.el.select(
                    rx.foreach(
                        AnalyticsState.date_range_options,
                        lambda opt: rx.el.option(opt, value=opt),
                    ),
                    value=AnalyticsState.date_range,
                    on_change=AnalyticsState.set_date_range,
                    class_name="text-sm font-medium border-gray-300 rounded-md shadow-sm",
                ),
                rx.el.button(
                    rx.icon("download", class_name="h-4 w-4 mr-2"),
                    "Export",
                    class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-black text-white hover:bg-black/90 h-10 px-4 py-2",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.foreach(AnalyticsState.key_metrics, metric_card),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3("Revenue Overview", class_name="text-lg font-semibold"),
                    rx.recharts.area_chart(
                        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                        rx.recharts.x_axis(data_key="month", hide=True),
                        rx.recharts.y_axis(hide=True),
                        rx.recharts.area(
                            type_="monotone",
                            data_key="revenue",
                            stroke="#3b82f6",
                            fill="#3b82f6",
                            fill_opacity=0.3,
                        ),
                        data=AnalyticsState.revenue_data,
                        height=350,
                        width="100%",
                    ),
                    class_name="p-6",
                ),
                class_name="bg-white rounded-xl border border-gray-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3("Top Products", class_name="text-lg font-semibold"),
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Product",
                                    class_name="text-left text-sm font-medium text-gray-500 py-2",
                                ),
                                rx.el.th(
                                    "Sales",
                                    class_name="text-right text-sm font-medium text-gray-500 py-2",
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                AnalyticsState.top_products,
                                lambda product: rx.el.tr(
                                    rx.el.td(
                                        product["name"], class_name="py-2 font-medium"
                                    ),
                                    rx.el.td(
                                        f"+{product['sales']}",
                                        class_name="py-2 text-right",
                                    ),
                                ),
                            )
                        ),
                        class_name="w-full mt-4",
                    ),
                    class_name="p-6",
                ),
                class_name="bg-white rounded-xl border border-gray-200 shadow-sm",
            ),
            class_name="grid gap-4 md:grid-cols-2",
        ),
        class_name="space-y-6",
    )


@rx.page(route="/analytics", title="Analytics")
def analytics() -> rx.Component:
    return main_layout(analytics_content())