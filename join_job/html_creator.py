from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device =1):
    style = 'style = "font-size:30px;"'
    html = '<html>\n <head></head>\n <bode>\n'
    html +='    <p {}>Temperature: {} C</p>\n'\
        .format(style, temperature_view(device))
    html +='    <p {}>Wind_speed: {} м/c</p>\n'\
        .format(style, wind_speed_view(device))
    html +='    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   </bode>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html