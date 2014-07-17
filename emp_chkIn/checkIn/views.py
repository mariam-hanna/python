from django.shortcuts import render_to_response
from django.template import RequestContext
from checkIn.models import chkInTime
import datetime 

def chkIn(request):
	context = RequestContext(request)
	diff = ''

	if request.method == 'POST':
		name = request.POST['name']
		checkInTime = request.POST['chkIn']
		
		inTime = datetime.time(9, 00).strftime("%I:%M")
		tooLate = datetime.time(10, 00).strftime("%I:%M")
		chkIn = checkInTime

		hour,minute = chkIn.split(":",2)	 

		if checkInTime > tooLate:
			message = "too late!"

		else:
			diff = 0
			if checkInTime > inTime:
				diff = datetime.datetime(2008, 3, 12,int(hour),int(minute),00) -  datetime.datetime(2008, 3, 12,9, 00,00)
				diff = str(diff).split(":")[1]+"min"
			message = "Good morning"
			chkIn_record = chkInTime(name=name,late=diff)
			chkIn_record.save()

		return render_to_response('checkIn/message.html',{'message':message,'diff':diff},context)

	else:
		return render_to_response('checkIn/chkInForm.html',{},context)


def showAttendance(request):
	context = RequestContext(request)
	attendance_records = chkInTime.objects.all()
	return render_to_response('checkIn/attendance.html',{'attendance_records':attendance_records},context)


