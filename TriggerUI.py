import justpy as jp
import numpy 

session_data = {}

def triggerui():
    wp = jp.WebPage()
    teststand = ['Teststand 1', 'Teststand 2']

    form1 = jp.Form(classes= 'h-screen', a=wp)

    # Title container on top
    title_container = jp.Div(classes='flex justify-center items-center bg-blue-500 h-20', a=form1)
    title_text = jp.P(text='Trigger UI', classes='text-white text-4xl', a=title_container)

    page_container = jp.Div(classes='flex flex-row h-70', a=form1)

    # Page container bottom line 
    container = jp.Div(classes="border-b-2 border-black bg-gray-200 pb-2", style="w-screen", a=form1)
 #---------------------------------------------------------------------------------------------------------------------------------------

    # Left container
    left_container = jp.Div(classes='flex-1 h-70 bg-gray-200 flex flex-col', a=page_container)

    # Radios for existing test cases
    def radio_button():
        teststands = ['Teststand 1', 'Teststand 2', 'Teststand 3']

        outer_div = jp.Div(classes='border m-2 p-2 w-32', a=left_container)

        jp.P(a=outer_div, text= 'Please select your teststand:')
        gender_list = []
        for teststand in teststands:
            label = jp.Label(classes='inline-block mb-1 p-1', a=outer_div)
            btn = jp.Input(type='radio', name='radio', value=teststand, a=label)
            gender_list.append(btn)
            jp.Span(classes='m1.-1', a=label, text=teststand.capitalize())

    radio_button()

    # Dropdown menu for test cases
    existing_test_dropdown = jp.Label(for_='testcases', text='Existing Test Cases', classes='text-2xl m-2', a=left_container)
    dropdown = jp.Select(name='testcases', id='testcases1', classes='m-2', a=left_container)
    option_select = jp.Option(text='Please select a test case', selected=True, disabled=True)
    option_1 = jp.Option(text='Test 1')
    option_2 = jp.Option(text='Test 2')
    option_3 = jp.Option(text='Test 3')
    option_4 = jp.Option(text='Test 4')
    
    dropdown.add(option_select, option_1, option_2, option_3, option_4)

    submit_button = jp.Input(value='Submit Form', type='submit', a=left_container)

    #----------------------------------------------------------------------------------------------------------------------

    # Right container
    right_container = jp.Div(classes='flex-1 h-70 bg-gray-200 flex flex-col', a=page_container)

    # Dropdown menu for new test cases
    new_test_dropdown = jp.Label(for_='testcases', text='New Test Cases', classes='text-2xl m-2', a=right_container)
    dropdown = jp.Select(name='testcases', id='testcases2', classes='m-2', a=right_container)
    option_select = jp.Option(text='Please select a test case', selected=True, disabled=True)
    option_1 = jp.Option(text='Test Category 1')
    option_2 = jp.Option(text='Test Category 2')
    option_3 = jp.Option(text='Test Category 3')
    option_4 = jp.Option(text='Test Category 4')
    
    dropdown.add(option_select, option_1, option_2, option_3, option_4)

    submit_button = jp.Input(value='Submit Form', type='submit', a=right_container)



    def submit_form(self, msg):
        print(msg)
        msg.page.redirect = '/form_submitted'
        session_data[msg.session_id] = msg.form_data

    form1.on('submit', submit_form)

    #----------------------------------------------------------------------------------------------------------------------

    # Bottom container for queue

    bottom_container = jp.Div(classes='flex-1 h-screen bg-gray-200 flex flex-col', a=form1)

    test_label = jp.Label(text='Test Cases Queue', classes='text-2xl m-2', a=bottom_container)

    

    #----------------------------------------------------------------------------------------------------------------------

    # temporary frames for containers
    #left_container_border = jp.Div(classes='border-2 border-black h-full', a=left_container)
    #right_container_border = jp.Div(classes='border-2 border-black h-full', a=right_container)
   
    return wp

jp.justpy(triggerui)