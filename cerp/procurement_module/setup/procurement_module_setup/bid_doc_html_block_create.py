from cerp.procurement_module.setup.default_setup_methods.create_html_block import create_html_block


def name_email_create_html_block():
    return create_html_block(
        name="info_about_user",

        html="""<div id="user-info">
                    <div id="full_name"></div>
                    <div id="email"></div>
                    </div>""",

        css="""#user-info {
                display: flex;
                gap: 10px; /* space between name and email */
                align-items: center; /* vertically center items */
                }

                #full_name, #email {
                padding: 8px 15px;
                background-color: #cce5ff; /* subtle blue background */
                border-radius: 6px;
                font-family: Arial, sans-serif;
                font-size: 18px; /* increased font size */
                color: #1a1a1a;
                font-weight: 600;
                }""",

        js="""frappe.call({
                method: "frappe.client.get",
                    args: {
                        doctype: "User",
                        name: frappe.session.user,
                        },
                        callback(r) {
                            if(r.message) {
                                root_element.querySelector("#full_name").textContent=r.message.full_name;
                                root_element.querySelector('#email').textContent=r.message.email;
                            }
                        }
            });"""
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