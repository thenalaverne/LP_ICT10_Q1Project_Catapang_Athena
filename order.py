from pyscript import display

def create_order():
    name = Element("custName").value
    address = Element("custAddr").value
    contact = Element("custNum").value

    total = 3.99 + 4.99 + 5.99 + 9.99
    summary = f"""
    <b>Order for:</b> {name}<br>
    <b>Address:</b> {address}<br>
    <b>Contact:</b> {contact}<br>
    <b>Total:</b> €{total:.2f}
    """
    display(summary, target="summary", append=False)