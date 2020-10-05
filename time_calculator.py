def add_time(*inputsTime):
  new_time = 'dump value'
  #start by spliting up all the data we get from the user


  #we expect either time, am/ap in [0] and time in [1], possible day [2]
  temp = inputsTime[0].split()
  startTime = temp[0] #start time
  startMeridiem = temp[1] #am/pm
  currentMeridiem = startMeridiem #for finding out the total am/pm
  totalHour = 0
  totalMin = 0
  days = 0
  counterOfWeek = 0
  finalDay = 'null'
  week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  #now get the time to add
  moreTime = inputsTime[1]


  #now if user adds a start day of the week
  try:
    startDay = inputsTime[2].lower()
  except:
    startDay = 'none'
  #now split the time and change to numbers
  temp = startTime.split(":")
  startHour = int(temp[0])
  startMin = int(temp[1])
  #now change to mill time and add 12 hours if pm
  if startMeridiem == 'PM':
    startHour = startHour + 12

  #now split the add Time
  temp = moreTime.split(":")
  addHour = int(temp[0])
  addMin = int(temp[1])

  #now we add the time and sort out the days 
  totalHour = startHour + addHour
  totalMin = startMin + addMin
  #start with min since min cant pass 60
  if totalMin >= 60:
    totalHour = totalHour + 1
    totalMin = totalMin % 60
  #now find the hours to days
  while totalHour >= 24:
    totalHour = totalHour - 24
    days = days + 1
  #now find the correct time and change form mil time if nessary
  if totalHour > 12:
    #mark for pm
    totalHour = totalHour - 12
    currentMeridiem = 'PM'
    
  elif totalHour == 12:
    currentMeridiem = 'PM'
  elif totalHour == 0:
    currentMeridiem = 'AM'
    totalHour = 12
  else:
    currentMeridiem = 'AM'
  
  #now trace the days
  try:
    temp = inputsTime[2]#trigger for time
    #lower case the day 
    for dayOfWeek in week:
      if dayOfWeek.lower() == startDay:
        #print(counterOfWeek)
        break
      counterOfWeek = counterOfWeek + 1
    #now we have the start day and now find the stop day
    if days % 7 == 0:
      finalDay = ', ' + week[counterOfWeek]
      if days > 0:
        finalDay = finalDay + ' ' + '('+str(days) + ' days later'+ ')'
    else:
      counterOfWeekTotal = counterOfWeek + days
      finalDay = ', ' + week[counterOfWeekTotal % 7]
      if days == 1:
        finalDay = finalDay + ' (next day)'
      else: 
        finalDay = finalDay + ' (' + str(days) + ' days later)'
  except:
    if days == 1:
      finalDay = ' (next day)'
    elif days > 1:
      finalDay = ' (' + str(days) + ' days later)'
    else:
      finalDay = ""

  
  if totalMin <= 9:
    new_time = str(totalHour) + ':0' + str(totalMin) + ' ' + currentMeridiem + finalDay
  else:
    new_time = str(totalHour) + ':' + str(totalMin) + ' ' + currentMeridiem + finalDay
  


  return new_time