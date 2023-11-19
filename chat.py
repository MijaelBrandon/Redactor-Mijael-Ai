
import pdfkit
import jinja2
from datetime import datetime
from openai import OpenAI

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

messages=[{ "role": "system", "content": "en un solo parrafo debes redactar solo la parte de peticion de una solicitud" }]
content = input("Bienvenido a tu asistente de Redaccion AI. /n Indica el documento que vamos a redactar:")
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{ "role": "user", "content": content }],
    
)

print(chat_completion.choices[0].message.content)




item_nombre = "Frank Andrade"
item_apellido = "Mueble"
item_dni = "Mueble"
item_direccion = "Lavadora"
item_ciudad = "Lavadora"
item_email = "Lavadora"
item_celular = "Lavadora"
today_date = datetime.today().strftime("%d %b, %Y")
item_cuerpo = chat_completion.choices[0].message.content


context = {'item_nombre': item_nombre,  'item_apellido': item_apellido, 'item_dni': item_dni,'item_direccion': item_direccion,
           'item_ciudad': item_ciudad, 'item_email': item_email, 'item_celular': item_celular, 
           'today_date': today_date, 'item_cuerpo': item_cuerpo}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'plantilla.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
output_pdf = 'pdf_generado.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='estilo.css')