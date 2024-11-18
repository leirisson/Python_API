from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        aluno = {
            'id':'1',
            'nome':'Leirisson'
        }
    return JsonResponse(aluno)

