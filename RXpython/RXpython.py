import subprocess
import sys

# Usa el intérprete de Python actual
python_executable = sys.executable

# Ejecutar generate_image.py
subprocess.run([python_executable, r"C:\Users\janus\OneDrive\Documentos\droplaipc\rx1\RXpython\PythonFIles\ge"
                                   r"nerate_image.py"])

import reflex as rx

def create_navigation_link(link_text):
    """Creates a navigation link with hover effects and transition properties."""
    return rx.el.a(
        link_text,
        href="#",
        transition_duration="300ms",
        _hover={"color": "#de3e1c"},
        color="#ffffff",
        transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_navigation_list_item(link_text):
    """Creates a list item containing a navigation link."""
    return rx.el.li(
        create_navigation_link(link_text=link_text)
    )


def create_section_heading(
    font_size, line_height, heading_text
):
    """Creates a section heading with customizable font size and line height."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="0.5rem",
        font_size=font_size,
        line_height=line_height,
        as_="h2",
    )


def create_paragraph(paragraph_text):
    """Creates a paragraph of text with a specific color."""
    return rx.text(paragraph_text, color="#060606")


def create_content_box(
    heading_font_size,
    heading_line_height,
    heading_text,
    text_button1,
    text_button2
):
    """Creates a content box with a heading and paragraph, styled with background color and box shadow."""
    return rx.box(
        create_section_heading(
            font_size=heading_font_size,
            line_height=heading_line_height,
            heading_text=heading_text,
        ),
        rx.vstack(
            rx.button(text_button1, width="70%"),
            rx.button(text_button2, width="70%"),
            width="90%",
            height="auto",

        )
    )


def create_botton2(
        heading_font_size,
        heading_line_height,
        heading_text,
        text_button1,
):
    """Creates a content box with a heading and paragraph, styled with background color and box shadow."""
    return rx.box(
        create_section_heading(
            font_size=heading_font_size,
            line_height=heading_line_height,
            heading_text=heading_text,
        ),
        rx.vstack(
            rx.button(text_button1, width="70%"),
            width="90%",
            height="auto",
        )
    )

def create_we_recommend(
        heading_font_size,
        heading_line_height,
        heading_text,
        textoo,
):
    """Creates a content box with a heading and paragraph, styled with background color and box shadow."""
    return rx.box(
        create_section_heading(
            font_size=heading_font_size,
            line_height=heading_line_height,
            heading_text=heading_text,
        ),
        rx.vstack(
            rx.box(textoo, width="70%"),
            width="90%",
            height="auto",
        )
    )


def create_list_item(item_text):
    """Creates a simple list item."""
    return rx.el.li(item_text)


def create_company_header():
    """Creates a company header with logo and name."""
    return rx.flex(
        rx.image(
            alt="Company Logo",
            src="Datito-sinfondo-(500x500).png",
            height="2.5rem",
            margin_right="1rem",
        ),
        rx.heading(
            "Dataether Agricultura",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#1F2937",
            as_="h1",
        ),
        display="flex",
        align_items="center",
    )


def create_contact_button():
    """Creates a 'Contact Us' button with hover effects."""
    return rx.el.button(
        "Rimau",
        background_color="#45cead",
        transition_duration="300ms",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
        transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        bg="transparent",  # Hacemos el fondo del botón transparente
        background="center/cover url('Rectangulo - Rimau (1000 x 300 px).png')",
    )

# def create_contact_button():
#     return rx.button(
#         "Mi botón con imagen",
#         bg="transparent",  # Hacemos el fondo del botón transparente
#         background="center/cover url('Rectangulo - Rimau (1000 x 300 px).png')",
#     )

def create_mobile_menu():
    """Creates a mobile menu with contact button and hamburger icon."""
    return rx.flex(
        create_contact_button(),
        rx.box(
            rx.icon(
                tag="menu",
                height="1.5rem",
                color="#cc5298",
                width="1.5rem",
            ),
            display=rx.breakpoints({"768px": "none"}),
        ),
        display="flex",
        align_items="center",
        column_gap="1rem",
    )


def create_navigation_bar():
    """Creates a full navigation bar with logo, menu items, and mobile menu."""
    return rx.flex(
        create_company_header(),
        rx.box(
            rx.list(
                create_navigation_list_item(
                    link_text="Geodatos"
                ),
                create_navigation_list_item(
                    link_text="Riesgos"
                ),
                create_navigation_list_item(
                    link_text="Testimonios"
                ),
                rx.icon("menu"),
                display="flex",
                column_gap="1.5rem",
            ),
            display=rx.breakpoints(
                {"0px": "none", "768px": "block"}
            ),
        ),
        create_mobile_menu(),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_header_section():
    """Creates the entire header section with responsive design."""
    return rx.box(
        rx.box(
            create_navigation_bar(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            padding_top="1rem",
            padding_bottom="1rem",
        ),
        background_color="#000000",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_visual_element():
    """Creates a visual element with an image and styling."""
    return rx.box(
        rx.vstack(
            rx.text("This is our region. :(", color_scheme="indigo", width="100%", align="center", weight="bold"),
            rx.image(
                alt="Visual element complementing the design",
                src="ayacucho_final.jpg",
                height="auto",
                border_radius="1rem",
                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                width="100%",
            ),
            width="100%"
        ),
        margin_bottom="2rem",
        padding_left="1rem",
        padding_right="1rem",
        width=rx.breakpoints(
            {"0px": "100%", "768px": "33.333333%"}
        )
    )



def create_features_section():
    """Creates a section displaying multiple feature boxes."""
    return rx.box(
        rx.box(
            rx.select(["Huamanga", "Huanta", "La Mar", "Cangallo", "Vilcashuamán",
                        "Víctor Fajardo", "Huanca Sancos", "Sucre", "Lucanas",
                        "Parinacochas", "Paucar del Sara Sara"], label="Distrito"),
            rx.button(
                rx.icon(tag="heart"),
                "Like",
                color_scheme="red",
            ),
            rx.button(
                rx.icon(tag="heart"),
                "Ayacucho",
                color_scheme="plum",
            ),
            rx.image(
                alt="Visual element complementing the design",
                src="mapa peru ayacucho.png",
                height="auto",
                border_radius="1rem",
                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                width="20%",
                align="center"
            ),
            display="flex",
            flex_direction="column",
            gap="1rem",
            align_items="center",
        ),
        margin_bottom="2rem",
        margin_top="4rem",
        padding_left="1rem",
        padding_right="1rem",
        width=rx.breakpoints(
            {"0px": "100%", "768px": "33.333333%"}
        ),
    )


def create_news_section():
    """Creates a section displaying latest news items."""
    return rx.box(
        create_section_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            heading_text="Latest News",
        ),
        rx.list(
            create_list_item(
                item_text="Company Launches New Product Line"
            ),
            create_list_item(
                item_text="Expansion into European Markets"
            ),
            create_list_item(
                item_text="Partnership with Leading Tech Firm Announced"
            ),
            list_style_type="disc",
            list_style_position="inside",
            color="#4B5563",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_testimonial_section():
    """Creates a section displaying a client testimonial."""
    return rx.box(
        create_section_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            heading_text="Client Testimonial",
        ),
        rx.blockquote(
            '"Working with this company has transformed our business operations. Their innovative solutions and dedicated support team have been invaluable to our success."',
            font_style="italic",
            color="#4B5563",
        ),
        rx.text(
            "- John Doe, CEO of XYZ Corp",
            margin_top="0.5rem",
            color="#6B7280",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_call_to_action_button():
    """Creates a 'Get Started' call-to-action button with hover effects."""
    return rx.el.a(
        "Let's talk",
        href="#",
        background_color="#3B82F6",
        transition_duration="300ms",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_contact_section():
    """Creates a contact section with a call-to-action."""
    return rx.box(
        create_section_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            heading_text="Contact Us",
        ),
        rx.text(
            "Ready to take your business to the next level? Get in touch with our team today.",
            margin_bottom="1rem",
            color="#4B5563",
        ),
        create_call_to_action_button(),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_main_content_section():
    """Creates the main content section including welcome message, mission statement, news, testimonial, and contact sections."""
    return rx.box(
        rx.box(
            create_content_box(
                heading_font_size="1.5rem",
                heading_line_height="2rem",
                heading_text="Here is your data",
                text_button1="High temperature",
                text_button2="Low precipitation"
            ),
            create_botton2(
                heading_font_size="1.25rem",
                heading_line_height="1.75rem",
                heading_text="Here are the risks",
                text_button1="Warning! Pathogen risk",
            ),
            create_we_recommend(
                heading_font_size="1.25rem",
                heading_line_height="1.75rem",
                heading_text="We recommend",
                textoo="general recommendations",
            ),
            display="flex",
            flex_direction="column",
            gap="2rem",
        ),
        margin_bottom="2rem",
        padding_left="1rem",
        padding_right="1rem",
        width=rx.breakpoints(
            {"0px": "100%", "768px": "33.333333%"}
        ),
        background_color="#3B82F6",
    )


def create_page_content():
    """Creates the entire page content, combining visual elements, features, and main content sections."""
    return rx.box(
        rx.flex(
            create_visual_element(),
            create_features_section(),
            create_main_content_section(),
            margin_left="-1rem",
            margin_right="-1rem",
            display="flex",
            flex_wrap="wrap",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_landing_page():
    """Creates the complete landing page, including styles, header, and all content sections."""
    return rx.fragment(
        rx.script(src="https://cdn.tailwindcss.com"),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        rx.box(
            create_header_section(),
            create_page_content(),
            background_color="#F3F4F6",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
    )
def index():
    return create_landing_page()


app = rx.App()
app.add_page(index)
