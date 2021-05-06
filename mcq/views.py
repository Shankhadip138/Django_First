from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from mcq.models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# Create your views here.

def index(request):
    #return HttpResponse("Hi, this is my first Django View")
    latest_question_list=Question.objects.order_by('pub_date')
    #template=loader.get_template("mcq/index.html")
    context={ "latest_question_list":latest_question_list}
    #output=",".join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))
    #return HttpResponse(output)
    return render(request,'mcq/index.html',context)

def details(request,question_id):
    #return HttpResponse("You are at the details page of question {0}".format(question_id))
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question':question}
    except Question.DoesNotExist:
        raise Http404(".....Question does not exist.....")
    return render(request,"mcq/details.html",context)


def vote(request,question_id):
    #return HttpResponse("You are at the vote page of question {0}".format(question_id))
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError.Choice.DoesNotExist):
        return render(request,'mcq/details.html',{'question':question,'error_message':"No choice made"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mcq:results',args=(question.id,)))

def results(request,question_id):
    #return HttpResponse("You are at the result page of question {0}".format(question_id))
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'mcq/results.html',{'question':question})
