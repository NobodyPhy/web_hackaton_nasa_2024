
#
# """
# def create_navigation_link(link_text):
#     """Creates a navigation link with hover effects and transition properties."""
#     return rx.el.a(
#         link_text,
#         href="#",
#         transition_duration="300ms",
#         _hover={"color": "#2563EB"},
#         color="#4B5563",
#         transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )
#
#
# def create_navigation_list_item(link_text):
#     """Creates a list item containing a navigation link."""
#     return rx.el.li(
#         create_navigation_link(link_text=link_text)
#     )
#
#
# def create_section_heading(
#     font_size, line_height, heading_text
# ):
#     """Creates a section heading with customizable font size and line height."""
#     return rx.heading(
#         heading_text,
#         font_weight="700",
#         margin_bottom="1rem",
#         font_size=font_size,
#         line_height=line_height,
#         as_="h2",
#     )
#
#
# def create_paragraph(paragraph_text):
#     """Creates a paragraph of text with a specific color."""
#     return rx.text(paragraph_text, color="#4B5563")
#
#
# def create_content_box(
#     heading_font_size,
#     heading_line_height,
#     heading_text,
#     paragraph_text,
# ):
#     """Creates a content box with a heading and paragraph, styled with background color and box shadow."""
#     return rx.box(
#         create_section_heading(
#             font_size=heading_font_size,
#             line_height=heading_line_height,
#             heading_text=heading_text,
#         ),
#         create_paragraph(paragraph_text=paragraph_text),
#         background_color="#ffffff",
#         padding="1.5rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )
#
#
# def create_list_item(item_text):
#     """Creates a simple list item."""
#     return rx.el.li(item_text)
#
#
# def create_company_header():
#     """Creates a company header with logo and name."""
#     return rx.flex(
#         rx.image(
#             alt="Company Logo",
#             src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/JQvzDEsjALJdIdhEvBSUPOPVVxqrnwjKED8MEiFK1GjABC5E/out-0.webp",
#             height="2.5rem",
#             margin_right="0.75rem",
#         ),
#         rx.heading(
#             "Company Name",
#             font_weight="700",
#             font_size="1.5rem",
#             line_height="2rem",
#             color="#1F2937",
#             as_="h1",
#         ),
#         display="flex",
#         align_items="center",
#     )
#
#
# def create_contact_button():
#     """Creates a 'Contact Us' button with hover effects."""
#     return rx.el.button(
#         "Contact Us",
#         background_color="#3B82F6",
#         transition_duration="300ms",
#         _hover={"background-color": "#2563EB"},
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.25rem",
#         color="#ffffff",
#         transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )
#
#
# def create_mobile_menu():
#     """Creates a mobile menu with contact button and hamburger icon."""
#     return rx.flex(
#         create_contact_button(),
#         rx.box(
#             rx.icon(
#                 tag="menu",
#                 height="1.5rem",
#                 color="#4B5563",
#                 width="1.5rem",
#             ),
#             display=rx.breakpoints({"768px": "none"}),
#         ),
#         display="flex",
#         align_items="center",
#         column_gap="1rem",
#     )
#
#
# def create_navigation_bar():
#     """Creates a full navigation bar with logo, menu items, and mobile menu."""
#     return rx.flex(
#         create_company_header(),
#         rx.box(
#             rx.list(
#                 create_navigation_list_item(
#                     link_text="Home"
#                 ),
#                 create_navigation_list_item(
#                     link_text="About"
#                 ),
#                 create_navigation_list_item(
#                     link_text="Services"
#                 ),
#                 display="flex",
#                 column_gap="1.5rem",
#             ),
#             display=rx.breakpoints(
#                 {"0px": "none", "768px": "block"}
#             ),
#         ),
#         create_mobile_menu(),
#         display="flex",
#         align_items="center",
#         justify_content="space-between",
#     )
#
#
# def create_header_section():
#     """Creates the entire header section with responsive design."""
#     return rx.box(
#         rx.box(
#             create_navigation_bar(),
#             width="100%",
#             style=rx.breakpoints(
#                 {
#                     "640px": {"max-width": "640px"},
#                     "768px": {"max-width": "768px"},
#                     "1024px": {"max-width": "1024px"},
#                     "1280px": {"max-width": "1280px"},
#                     "1536px": {"max-width": "1536px"},
#                 }
#             ),
#             margin_left="auto",
#             margin_right="auto",
#             padding_left="1rem",
#             padding_right="1rem",
#             padding_top="1rem",
#             padding_bottom="1rem",
#         ),
#         background_color="#ffffff",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )
#
#
# def create_visual_element():
#     """Creates a visual element with an image and styling."""
#     return rx.box(
#         rx.image(
#             alt="Visual element complementing the design",
#             src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/h0GcmibYrxZlBdVRvYe85j3tTcyNZxJj3Mxd1tBVeJpG4HkTA/out-0.webp",
#             height="auto",
#             border_radius="0.5rem",
#             box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
#             width="100%",
#         ),
#         margin_bottom="2rem",
#         padding_left="1rem",
#         padding_right="1rem",
#         width=rx.breakpoints(
#             {"0px": "100%", "768px": "33.333333%"}
#         ),
#     )
# #
#
# def create_features_section():
#     """Creates a section displaying multiple feature boxes."""
#     return rx.box(
#         rx.box(
#             create_content_box(
#                 heading_font_size="1.25rem",
#                 heading_line_height="1.75rem",
#                 heading_text="Feature 1",
#                 paragraph_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#             ),
#             create_content_box(
#                 heading_font_size="1.25rem",
#                 heading_line_height="1.75rem",
#                 heading_text="Feature 2",
#                 paragraph_text="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
#             ),
#             create_content_box(
#                 heading_font_size="1.25rem",
#                 heading_line_height="1.75rem",
#                 heading_text="Feature 3",
#                 paragraph_text="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
#             ),
#             display="flex",
#             flex_direction="column",
#             gap="2rem",
#         ),
#         margin_bottom="2rem",
#         padding_left="1rem",
#         padding_right="1rem",
#         width=rx.breakpoints(
#             {"0px": "100%", "768px": "33.333333%"}
#         ),
#     )
#
#
# def create_news_section():
#     """Creates a section displaying latest news items."""
#     return rx.box(
#         create_section_heading(
#             font_size="1.25rem",
#             line_height="1.75rem",
#             heading_text="Latest News",
#         ),
#         rx.list(
#             create_list_item(
#                 item_text="Company Launches New Product Line"
#             ),
#             create_list_item(
#                 item_text="Expansion into European Markets"
#             ),
#             create_list_item(
#                 item_text="Partnership with Leading Tech Firm Announced"
#             ),
#             list_style_type="disc",
#             list_style_position="inside",
#             color="#4B5563",
#         ),
#         background_color="#ffffff",
#         padding="1.5rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )
#
#
# def create_testimonial_section():
#     """Creates a section displaying a client testimonial."""
#     return rx.box(
#         create_section_heading(
#             font_size="1.25rem",
#             line_height="1.75rem",
#             heading_text="Client Testimonial",
#         ),
#         rx.blockquote(
#             '"Working with this company has transformed our business operations. Their innovative solutions and dedicated support team have been invaluable to our success."',
#             font_style="italic",
#             color="#4B5563",
#         ),
#         rx.text(
#             "- John Doe, CEO of XYZ Corp",
#             margin_top="0.5rem",
#             color="#6B7280",
#         ),
#         background_color="#ffffff",
#         padding="1.5rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )
#
#
# def create_call_to_action_button():
#     """Creates a 'Get Started' call-to-action button with hover effects."""
#     return rx.el.a(
#         "Get Started",
#         href="#",
#         background_color="#3B82F6",
#         transition_duration="300ms",
#         _hover={"background-color": "#2563EB"},
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.25rem",
#         color="#ffffff",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )
#
#
# def create_contact_section():
#     """Creates a contact section with a call-to-action."""
#     return rx.box(
#         create_section_heading(
#             font_size="1.25rem",
#             line_height="1.75rem",
#             heading_text="Contact Us",
#         ),
#         rx.text(
#             "Ready to take your business to the next level? Get in touch with our team today.",
#             margin_bottom="1rem",
#             color="#4B5563",
#         ),
#         create_call_to_action_button(),
#         background_color="#ffffff",
#         padding="1.5rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )
#
#
# def create_main_content_section():
#     """Creates the main content section including welcome message, mission statement, news, testimonial, and contact sections."""
#     return rx.box(
#         rx.box(
#             create_content_box(
#                 heading_font_size="1.5rem",
#                 heading_line_height="2rem",
#                 heading_text="Welcome to Our Company",
#                 paragraph_text="We are dedicated to providing innovative solutions for your business needs. Our team of experts is committed to delivering excellence in every project.",
#             ),
#             create_content_box(
#                 heading_font_size="1.25rem",
#                 heading_line_height="1.75rem",
#                 heading_text="Our Mission",
#                 paragraph_text="To empower businesses with cutting-edge technology and unparalleled support, driving growth and success in the digital age.",
#             ),
#             create_news_section(),
#             create_testimonial_section(),
#             create_contact_section(),
#             display="flex",
#             flex_direction="column",
#             gap="2rem",
#         ),
#         margin_bottom="2rem",
#         padding_left="1rem",
#         padding_right="1rem",
#         width=rx.breakpoints(
#             {"0px": "100%", "768px": "33.333333%"}
#         ),
#     )
#
#
# def create_page_content():
#     """Creates the entire page content, combining visual elements, features, and main content sections."""
#     return rx.box(
#         rx.flex(
#             create_visual_element(),
#             create_features_section(),
#             create_main_content_section(),
#             margin_left="-1rem",
#             margin_right="-1rem",
#             display="flex",
#             flex_wrap="wrap",
#         ),
#         width="100%",
#         style=rx.breakpoints(
#             {
#                 "640px": {"max-width": "640px"},
#                 "768px": {"max-width": "768px"},
#                 "1024px": {"max-width": "1024px"},
#                 "1280px": {"max-width": "1280px"},
#                 "1536px": {"max-width": "1536px"},
#             }
#         ),
#         margin_left="auto",
#         margin_right="auto",
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="2rem",
#         padding_bottom="2rem",
#     )
#
#
# def create_landing_page():
#     """Creates the complete landing page, including styles, header, and all content sections."""
#     return rx.fragment(
#         rx.script(src="https://cdn.tailwindcss.com"),
#         rx.el.style(
#             """
#         @font-face {
#             font-family: 'LucideIcons';
#             src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
#         }
#     """
#         ),
#         rx.box(
#             create_header_section(),
#             create_page_content(),
#             background_color="#F3F4F6",
#             font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
#         ),
#     )
# """
#
#
#
#
#
#
