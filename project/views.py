from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def test(request):
    return render(request,'test.html')
@csrf_exempt
def index(request):

        HTML = render(request, 'index.html')
        if request.method=='POST':
            HTML.delete_cookie('NAME')
            HTML.delete_cookie('NON')
            return HTML
        HTML.set_cookie('NON', 'R{OIGJ{OIGJO{GOJGGOGHJDOUSPHGUSDGUUJSHGUHDGPGHNP{DNSG{PIJGN')

        HTML.set_cookie('NAME', 'Yroslav')
        return HTML
#ppppppppppppppppppppppppppppppp
