from cerp.procurement_module.setup.default_setup_methods.create_html_block import create_html_block


def name_email_create_html_block():
    return create_html_block(
        name="my_alert",
        html="<div class='alert'>Hello World!</div>",
        css=".alert { background: yellow; padding: 10px; }",
        js="console.log('Alert loaded');"
    )







# # Usage Example 1: Simple Alert
# create_html_block(
#     name="my_alert",
#     html="<div class='alert'>Hello World!</div>",
#     css=".alert { background: yellow; padding: 10px; }",
#     js="console.log('Alert loaded');"
# )

# # Usage Example 2: Interactive Button
# create_html_block(
#     name="my_button",
#     html="<button onclick='showMessage()'>Click Me</button>",
#     css="button { background: blue; color: white; padding: 10px; }",
#     js="function showMessage() { frappe.msgprint('Button clicked!'); }"
# )