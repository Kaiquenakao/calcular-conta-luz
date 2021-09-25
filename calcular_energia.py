import PySimpleGUI as sg


def interface():
    # Definindo tema
    sg.theme('Reddit')

    # Layout
    layout = [
        [sg.Text('Calcular conta de luz', font=('Helvetica', 15))],
        [sg.Text('Consumo (kWh)'), sg.Input(key='cxconsumo', size=(10, 1), pad=(10, 1))],
        [sg.Text('Tarifa (R$/kWh)'), sg.Input(key='cxtarifa', size=(10, 1), pad=(15, 1))],
        [sg.Text('Pis/Cofins em %'), sg.Input(key='cxpiscofins', size=(10, 1), pad=(8, 1))],
        [sg.Text('ICMS em %'), sg.Input(key='cxicsm', size=(10, 1), pad=(10, 1))],
        [sg.Button('Calcular', key='calcular', pad=(80, 5))],
        [sg.Text('Total'), sg.Input(key='cxtotal', disabled=True, size=(10, 1))]
    ]
    return sg.Window('Calcular conta de luz', layout=layout, finalize=True)


janela = interface()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'calcular':
        if values['cxtarifa'] != '' and values['cxpiscofins'] != '' \
                and values['cxicsm'] != '' and values['cxconsumo'] != '':

            taf_final = float(values['cxtarifa']) / \
                           (1 - ((float(values['cxpiscofins']) / 100) + (float(values['cxicsm']) / 100)))
            valor_total = round((taf_final * float(values['cxconsumo'])), 2)

            sg.popup("Resultado obtido")
            window['cxtotal'].Update(value=valor_total)

        else:
            sg.popup("Algum campo está vázio")
