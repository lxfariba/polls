from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect 
from django.template import loader
from django.utils import timezone


from .models import Question, Choice



def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	# output= ','.join([q.question_text for q in latest_question_list])
	# template = loader.get_template('polls/index.html')
	context = {
			'latest_question_list':latest_question_list
	}
	# return HttpResponse(template.render(request,context))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# return HttpResponse("You are looking at a question %s." % question_id)
	# try:
	# 	question = Question.objects.get(pk = question_id)
	# except Question.DoesNotExit
	# 	raise Http404("Question Does Not Exit!")
	# return render(request, 'polls/detail.html',{'question':question})	
	question = get_object_or_404(Question,pk=question_id)
	return render(request, 'polls/index.html', {'question':question})


		


def results(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk =request.POST['choice'])
	except (KeyError,Choice.DoesNotExit):
		return render(request,'polls/detail.html', {
			'question':question,
			'error_message':"you didn't select a choice!"
			})
	else:
		selected_choice.vote += 1
		selected_choice. save()
	return HttpResponseRedirect(reverse('polls:results' , args =(question.id,)))
