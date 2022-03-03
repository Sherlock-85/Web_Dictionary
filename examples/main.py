import justpy as jp

# Create a webpage instance
@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4")
    in_1 = jp.Input(a=div1, placeholder="Enter first value",
             classes="form-input")
    in_2 = jp.Input(a=div1, placeholder="Enter second value",
             classes="form-input")
    d_output = jp.Div(a=div1, text="Result goes here...", classes="text-purple-600")
    jp.Div(a=div1, text="Another div...", classes="text-purple-600")
    jp.Div(a=div1, text="And another div...", classes="text-purple-600")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div2, Text="Calculate", click=sum_up, in1=in_1, in2=in_2,
              d=d_output,
              classes="border-4 border-green-300 m-2 py-1 px-4 rounded "
              "text-blue-600 hover:bg-red-500 hover:text-black")
    jp.Div(a=div2, text="I am an amazing interactive div!", mouseenter=mouse_enter,
           mouseleave=mouse_leave,
           classes="hover:bg-red-500")
    # jp.Div(a=wp, text="This is a div!",
    #        classes="text-green-400 bg-yellow-500")
    # jp.Div(a=wp, text="This is another div!")
    return wp

def sum_up(widget, msg):
    sum = float(widget.in1.value)+ float(widget.in2.value)
    widget.d.text = sum

def mouse_enter(widget,msg):
    widget.text = "A mouse has entered the house!"

def mouse_leave(widget, msg):
    widget.text = "The mouse left the house!"



# jp.Route("/home", home)
jp.justpy()