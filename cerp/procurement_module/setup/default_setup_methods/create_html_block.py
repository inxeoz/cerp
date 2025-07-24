import frappe

@frappe.whitelist()
def create_html_block(name, html, css="", js=""):
    """Create HTML block using the correct field names"""
    
    try:
        # Check if document exists
        if frappe.db.exists("Custom HTML Block", name):
            # Update existing
            doc = frappe.get_doc("Custom HTML Block", name)
        else:
            # Create new
            doc = frappe.new_doc("Custom HTML Block")
            doc.name = name
        
        # Set the fields with correct names
        doc.html = html
        doc.style = css
        doc.script = js
        doc.private = 0  # Make it public by default
        
        # Save the document
        doc.save(ignore_permissions=True)
        frappe.db.commit()
        
        return {
            "success": True,
            "name": name,
            "message": f"HTML Block '{name}' created successfully"
        }
        
    except Exception as e:
        frappe.log_error(f"Error creating HTML block: {str(e)}")
        return {
            "success": False,
            "error": str(e)
        }

# # Your function should now work
# def name_email_create_html_block():
#     return create_html_block(
#         name="my_alert",
#         html="<div class='alert'>Hello World!</div>",
#         css=".alert { background: yellow; padding: 10px; }",
#         js="console.log('Alert loaded');"
#     )



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