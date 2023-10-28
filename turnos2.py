import mechanicalsoup
import time
import re
import datetime
import TurnoService
import io


def get_date_and_time(text):
  """
  Obtiene la fecha y hora inicial y final de una cadena de texto utilizando una expresión regular.

  Args:
    text: La cadena de texto que contiene la fecha y hora.

  Returns:
    Una tupla con la fecha y hora inicial y final.
  """

  # Obtener la expresión regular para la fecha y hora.
  regex = r"(?P<date>(?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/(?:19\d\d|20\d\d)) (?P<time>(?:[0-2]\d):(?:[0-5]\d))"

  # Extraer la fecha y hora inicial y final de la cadena de texto.
  match = re.findall(regex,text)

  # Obtener la fecha y hora inicial.
  date_and_time_initial = match[0][0] + " " + match[0][1]

  # Obtener la fecha y hora final.
  date_and_time_final = match[1][0] + " " + match[1][1]

  # Convertir la fecha y hora inicial a un objeto datetime.
  date_and_time_initial = datetime.datetime.strptime(date_and_time_initial, "%d/%m/%Y %H:%M")

  # Convertir la fecha y hora final a un objeto datetime.
  date_and_time_final = datetime.datetime.strptime(date_and_time_final, "%d/%m/%Y %H:%M")

  # Devolver la fecha y hora inicial y final.
  return date_and_time_initial, date_and_time_final

def print_turns(turno):
  """
  Imprime en formato legible los turnos devueltos por la función `get_date_and_time()`.

  Args:
    date_and_time_initial: La fecha y hora inicial del turno.
    date_and_time_final: La fecha y hora final del turno.
  """

  # Obtener la fecha y hora inicial en formato legible.
  date_and_time_initial_readable = turno[0].strftime("%d/%m/%Y %H:%M")

  # Obtener la fecha y hora final en formato legible.
  date_and_time_final_readable = turno[1].strftime("%d/%m/%Y %H:%M")

  # Imprimir el turno en formato legible.
  return f"Turno: {date_and_time_initial_readable} - {date_and_time_final_readable}"


def enviarNotificacion(message):
    print("Se dispara notificacion")
    import requests
    requests.post("https://ntfy.sh/",data=message.encode(encoding='utf-8'))

def getTurnos():
    turnos = []
    url = "https://irrigaciondiamante.com/login/turnosdiamante.php"
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    login_html = login_page.soup

    # 2
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = ""

    time.sleep(2)

    # 3
    profiles_page = browser.submit(form, login_page.url)

    form1 = profiles_page.soup.select("form")[0]

    data_page = browser.submit(form1, profiles_page.url)

    items = data_page.soup.findAll("p",class_="titulo_turno")

    i = 10
    max = len(items)
    while i < max:
        turnos.append(items[i].text)
        i += 1
    turnosN = list(filter(lambda x: x.find("/2023") > 0, turnos))

    return turnosN

turnos = getTurnos()
message = ""
for t in turnos:
    t1 = get_date_and_time(t)
    existe = TurnoService.existeTurno(t1)
    if existe == None:
        TurnoService.saveTurnos(t1)
        print(f"Turno Guardado: {print_turns(t1)}")
        message += print_turns(t1)+"\n"
    else:
        print(f"Turno existente: {print_turns(t1)}")
    
if len(message) > 0:
    enviarNotificacion(message)
else:
    print("No existe nuevos turnos")