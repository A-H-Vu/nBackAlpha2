#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 25, 2020, at 15:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'n-back-testing'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\n-back-alpha2\\nBackAlpha2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='In this task you will be required to press space if the white square appeared in the same location as the location on the last trial. For example if the square was in the left down corner on trial 1 and then it appeared in the same location on trial 2, press space. Otherwise, do not respond. Press space to continue.',
    font='Arial',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
trial1Grid = visual.ImageStim(
    win=win,
    name='trial1Grid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trial1Square = visual.Rect(
    win=win, name='trial1Square',
    width=[0.15,0.15][0], height=[0.15,0.15][1],
    ori=0.0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trial1Fix = visual.TextStim(win=win, name='trial1Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trial1Resp = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='This is the end of N-back-1 trials. You are about to start N-back-2 trials. This means that instead of pressing space whenever the square appears in the same position as on the position on one trial before, you are required to press space whenever the square appears in the same position as on the position two trials before. For example if the square appeared in left down corner on trial 1, you should press space if the square appears in the left down corner on trial 3. Press space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp2 = keyboard.Keyboard()

# Initialize components for Routine "fixation2"
fixation2Clock = core.Clock()
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
trial2Grid = visual.ImageStim(
    win=win,
    name='trial2Grid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trial2Square = visual.Rect(
    win=win, name='trial2Square',
    width=[0.15,0.15][0], height=[0.15,0.15][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trial2Fix = visual.TextStim(win=win, name='trial2Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trial2Resp = keyboard.Keyboard()

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
instr3 = visual.TextStim(win=win, name='instr3',
    text='This is the end of N-back-2 trials. You are about to start N-back-3 trials. This means that instead of pressing space whenever the square appears in the same position as on the position on two trials before, you are required to press space whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press space if the square appears in the left down corner on trial 4. Press space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp3 = keyboard.Keyboard()

# Initialize components for Routine "fixation3"
fixation3Clock = core.Clock()
fix3 = visual.TextStim(win=win, name='fix3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial3"
trial3Clock = core.Clock()
trial3Grid = visual.ImageStim(
    win=win,
    name='trial3Grid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trial3Square = visual.Rect(
    win=win, name='trial3Square',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trial3Fix = visual.TextStim(win=win, name='trial3Fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trial3Resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='This is the end of the experiment.\nThank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instructions1Components = [instr1, keyResp1]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if keyResp1.keys in ['', [], None]:  # No response was made
    keyResp1.keys = None
thisExp.addData('keyResp1.keys',keyResp1.keys)
if keyResp1.keys != None:  # we had a response
    thisExp.addData('keyResp1.rt', keyResp1.rt)
thisExp.addData('keyResp1.started', keyResp1.tStartRefresh)
thisExp.addData('keyResp1.stopped', keyResp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [fix1]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation1"-------
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackCond1.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trial1Square.setPos([loc1,loc2])
    trial1Resp.keys = []
    trial1Resp.rt = []
    _trial1Resp_allKeys = []
    # keep track of which components have finished
    trial1Components = [trial1Grid, trial1Square, trial1Fix, trial1Resp]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial1Grid* updates
        if trial1Grid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Grid.frameNStart = frameN  # exact frame index
            trial1Grid.tStart = t  # local t and not account for scr refresh
            trial1Grid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Grid, 'tStartRefresh')  # time at next scr refresh
            trial1Grid.setAutoDraw(True)
        if trial1Grid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Grid.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trial1Grid.tStop = t  # not accounting for scr refresh
                trial1Grid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Grid, 'tStopRefresh')  # time at next scr refresh
                trial1Grid.setAutoDraw(False)
        
        # *trial1Square* updates
        if trial1Square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Square.frameNStart = frameN  # exact frame index
            trial1Square.tStart = t  # local t and not account for scr refresh
            trial1Square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Square, 'tStartRefresh')  # time at next scr refresh
            trial1Square.setAutoDraw(True)
        if trial1Square.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Square.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1Square.tStop = t  # not accounting for scr refresh
                trial1Square.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Square, 'tStopRefresh')  # time at next scr refresh
                trial1Square.setAutoDraw(False)
        
        # *trial1Fix* updates
        if trial1Fix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Fix.frameNStart = frameN  # exact frame index
            trial1Fix.tStart = t  # local t and not account for scr refresh
            trial1Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Fix, 'tStartRefresh')  # time at next scr refresh
            trial1Fix.setAutoDraw(True)
        if trial1Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial1Fix.tStop = t  # not accounting for scr refresh
                trial1Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Fix, 'tStopRefresh')  # time at next scr refresh
                trial1Fix.setAutoDraw(False)
        
        # *trial1Resp* updates
        waitOnFlip = False
        if trial1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Resp.frameNStart = frameN  # exact frame index
            trial1Resp.tStart = t  # local t and not account for scr refresh
            trial1Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Resp, 'tStartRefresh')  # time at next scr refresh
            trial1Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial1Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial1Resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial1Resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trial1Resp.tStop = t  # not accounting for scr refresh
                trial1Resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial1Resp, 'tStopRefresh')  # time at next scr refresh
                trial1Resp.status = FINISHED
        if trial1Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial1Resp.getKeys(keyList=['space'], waitRelease=False)
            _trial1Resp_allKeys.extend(theseKeys)
            if len(_trial1Resp_allKeys):
                trial1Resp.keys = _trial1Resp_allKeys[-1].name  # just the last key pressed
                trial1Resp.rt = _trial1Resp_allKeys[-1].rt
                # was this correct?
                if (trial1Resp.keys == str(corrAns)) or (trial1Resp.keys == corrAns):
                    trial1Resp.corr = 1
                else:
                    trial1Resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials1.addData('trial1Grid.started', trial1Grid.tStartRefresh)
    trials1.addData('trial1Grid.stopped', trial1Grid.tStopRefresh)
    trials1.addData('trial1Square.started', trial1Square.tStartRefresh)
    trials1.addData('trial1Square.stopped', trial1Square.tStopRefresh)
    trials1.addData('trial1Fix.started', trial1Fix.tStartRefresh)
    trials1.addData('trial1Fix.stopped', trial1Fix.tStopRefresh)
    # check responses
    if trial1Resp.keys in ['', [], None]:  # No response was made
        trial1Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial1Resp.corr = 1;  # correct non-response
        else:
           trial1Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials1 (TrialHandler)
    trials1.addData('trial1Resp.keys',trial1Resp.keys)
    trials1.addData('trial1Resp.corr', trial1Resp.corr)
    if trial1Resp.keys != None:  # we had a response
        trials1.addData('trial1Resp.rt', trial1Resp.rt)
    trials1.addData('trial1Resp.started', trial1Resp.tStartRefresh)
    trials1.addData('trial1Resp.stopped', trial1Resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
keyResp2.keys = []
keyResp2.rt = []
_keyResp2_allKeys = []
# keep track of which components have finished
instructions2Components = [instr2, keyResp2]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *keyResp2* updates
    waitOnFlip = False
    if keyResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp2.frameNStart = frameN  # exact frame index
        keyResp2.tStart = t  # local t and not account for scr refresh
        keyResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp2, 'tStartRefresh')  # time at next scr refresh
        keyResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp2.status == STARTED and not waitOnFlip:
        theseKeys = keyResp2.getKeys(keyList=['space'], waitRelease=False)
        _keyResp2_allKeys.extend(theseKeys)
        if len(_keyResp2_allKeys):
            keyResp2.keys = _keyResp2_allKeys[-1].name  # just the last key pressed
            keyResp2.rt = _keyResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr2.started', instr2.tStartRefresh)
thisExp.addData('instr2.stopped', instr2.tStopRefresh)
# check responses
if keyResp2.keys in ['', [], None]:  # No response was made
    keyResp2.keys = None
thisExp.addData('keyResp2.keys',keyResp2.keys)
if keyResp2.keys != None:  # we had a response
    thisExp.addData('keyResp2.rt', keyResp2.rt)
thisExp.addData('keyResp2.started', keyResp2.tStartRefresh)
thisExp.addData('keyResp2.stopped', keyResp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation2Components = [fix2]
for thisComponent in fixation2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix2* updates
    if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix2.frameNStart = frameN  # exact frame index
        fix2.tStart = t  # local t and not account for scr refresh
        fix2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
        fix2.setAutoDraw(True)
    if fix2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix2.tStop = t  # not accounting for scr refresh
            fix2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
            fix2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation2"-------
for thisComponent in fixation2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix2.started', fix2.tStartRefresh)
thisExp.addData('fix2.stopped', fix2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackCond2.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trial2Square.setPos([loc1,loc2])
    trial2Resp.keys = []
    trial2Resp.rt = []
    _trial2Resp_allKeys = []
    # keep track of which components have finished
    trial2Components = [trial2Grid, trial2Square, trial2Fix, trial2Resp]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial2Grid* updates
        if trial2Grid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Grid.frameNStart = frameN  # exact frame index
            trial2Grid.tStart = t  # local t and not account for scr refresh
            trial2Grid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Grid, 'tStartRefresh')  # time at next scr refresh
            trial2Grid.setAutoDraw(True)
        if trial2Grid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Grid.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Grid.tStop = t  # not accounting for scr refresh
                trial2Grid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Grid, 'tStopRefresh')  # time at next scr refresh
                trial2Grid.setAutoDraw(False)
        
        # *trial2Square* updates
        if trial2Square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Square.frameNStart = frameN  # exact frame index
            trial2Square.tStart = t  # local t and not account for scr refresh
            trial2Square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Square, 'tStartRefresh')  # time at next scr refresh
            trial2Square.setAutoDraw(True)
        if trial2Square.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Square.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Square.tStop = t  # not accounting for scr refresh
                trial2Square.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Square, 'tStopRefresh')  # time at next scr refresh
                trial2Square.setAutoDraw(False)
        
        # *trial2Fix* updates
        if trial2Fix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Fix.frameNStart = frameN  # exact frame index
            trial2Fix.tStart = t  # local t and not account for scr refresh
            trial2Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Fix, 'tStartRefresh')  # time at next scr refresh
            trial2Fix.setAutoDraw(True)
        if trial2Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Fix.tStop = t  # not accounting for scr refresh
                trial2Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Fix, 'tStopRefresh')  # time at next scr refresh
                trial2Fix.setAutoDraw(False)
        
        # *trial2Resp* updates
        waitOnFlip = False
        if trial2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Resp.frameNStart = frameN  # exact frame index
            trial2Resp.tStart = t  # local t and not account for scr refresh
            trial2Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Resp, 'tStartRefresh')  # time at next scr refresh
            trial2Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial2Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial2Resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial2Resp.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                trial2Resp.tStop = t  # not accounting for scr refresh
                trial2Resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial2Resp, 'tStopRefresh')  # time at next scr refresh
                trial2Resp.status = FINISHED
        if trial2Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial2Resp.getKeys(keyList=['space'], waitRelease=False)
            _trial2Resp_allKeys.extend(theseKeys)
            if len(_trial2Resp_allKeys):
                trial2Resp.keys = _trial2Resp_allKeys[-1].name  # just the last key pressed
                trial2Resp.rt = _trial2Resp_allKeys[-1].rt
                # was this correct?
                if (trial2Resp.keys == str(corrAns)) or (trial2Resp.keys == corrAns):
                    trial2Resp.corr = 1
                else:
                    trial2Resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('trial2Grid.started', trial2Grid.tStartRefresh)
    trials2.addData('trial2Grid.stopped', trial2Grid.tStopRefresh)
    trials2.addData('trial2Square.started', trial2Square.tStartRefresh)
    trials2.addData('trial2Square.stopped', trial2Square.tStopRefresh)
    trials2.addData('trial2Fix.started', trial2Fix.tStartRefresh)
    trials2.addData('trial2Fix.stopped', trial2Fix.tStopRefresh)
    # check responses
    if trial2Resp.keys in ['', [], None]:  # No response was made
        trial2Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial2Resp.corr = 1;  # correct non-response
        else:
           trial2Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials2 (TrialHandler)
    trials2.addData('trial2Resp.keys',trial2Resp.keys)
    trials2.addData('trial2Resp.corr', trial2Resp.corr)
    if trial2Resp.keys != None:  # we had a response
        trials2.addData('trial2Resp.rt', trial2Resp.rt)
    trials2.addData('trial2Resp.started', trial2Resp.tStartRefresh)
    trials2.addData('trial2Resp.stopped', trial2Resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


# ------Prepare to start Routine "instructions3"-------
continueRoutine = True
# update component parameters for each repeat
keyResp3.keys = []
keyResp3.rt = []
_keyResp3_allKeys = []
# keep track of which components have finished
instructions3Components = [instr3, keyResp3]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr3* updates
    if instr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr3.frameNStart = frameN  # exact frame index
        instr3.tStart = t  # local t and not account for scr refresh
        instr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr3, 'tStartRefresh')  # time at next scr refresh
        instr3.setAutoDraw(True)
    
    # *keyResp3* updates
    waitOnFlip = False
    if keyResp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp3.frameNStart = frameN  # exact frame index
        keyResp3.tStart = t  # local t and not account for scr refresh
        keyResp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp3, 'tStartRefresh')  # time at next scr refresh
        keyResp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp3.status == STARTED and not waitOnFlip:
        theseKeys = keyResp3.getKeys(keyList=['space'], waitRelease=False)
        _keyResp3_allKeys.extend(theseKeys)
        if len(_keyResp3_allKeys):
            keyResp3.keys = _keyResp3_allKeys[-1].name  # just the last key pressed
            keyResp3.rt = _keyResp3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr3.started', instr3.tStartRefresh)
thisExp.addData('instr3.stopped', instr3.tStopRefresh)
# check responses
if keyResp3.keys in ['', [], None]:  # No response was made
    keyResp3.keys = None
thisExp.addData('keyResp3.keys',keyResp3.keys)
if keyResp3.keys != None:  # we had a response
    thisExp.addData('keyResp3.rt', keyResp3.rt)
thisExp.addData('keyResp3.started', keyResp3.tStartRefresh)
thisExp.addData('keyResp3.stopped', keyResp3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation3Components = [fix3]
for thisComponent in fixation3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix3* updates
    if fix3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix3.frameNStart = frameN  # exact frame index
        fix3.tStart = t  # local t and not account for scr refresh
        fix3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix3, 'tStartRefresh')  # time at next scr refresh
        fix3.setAutoDraw(True)
    if fix3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix3.tStop = t  # not accounting for scr refresh
            fix3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix3, 'tStopRefresh')  # time at next scr refresh
            fix3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation3"-------
for thisComponent in fixation3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix3.started', fix3.tStartRefresh)
thisExp.addData('fix3.stopped', fix3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackCond3.xlsx'),
    seed=None, name='trials3')
thisExp.addLoop(trials3)  # add the loop to the experiment
thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
if thisTrials3 != None:
    for paramName in thisTrials3:
        exec('{} = thisTrials3[paramName]'.format(paramName))

for thisTrials3 in trials3:
    currentLoop = trials3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3:
            exec('{} = thisTrials3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial3"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trial3Square.setPos([loc1,loc2])
    trial3Resp.keys = []
    trial3Resp.rt = []
    _trial3Resp_allKeys = []
    # keep track of which components have finished
    trial3Components = [trial3Grid, trial3Square, trial3Fix, trial3Resp]
    for thisComponent in trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial3Grid* updates
        if trial3Grid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial3Grid.frameNStart = frameN  # exact frame index
            trial3Grid.tStart = t  # local t and not account for scr refresh
            trial3Grid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3Grid, 'tStartRefresh')  # time at next scr refresh
            trial3Grid.setAutoDraw(True)
        if trial3Grid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial3Grid.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                trial3Grid.tStop = t  # not accounting for scr refresh
                trial3Grid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial3Grid, 'tStopRefresh')  # time at next scr refresh
                trial3Grid.setAutoDraw(False)
        
        # *trial3Square* updates
        if trial3Square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial3Square.frameNStart = frameN  # exact frame index
            trial3Square.tStart = t  # local t and not account for scr refresh
            trial3Square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3Square, 'tStartRefresh')  # time at next scr refresh
            trial3Square.setAutoDraw(True)
        if trial3Square.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial3Square.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial3Square.tStop = t  # not accounting for scr refresh
                trial3Square.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial3Square, 'tStopRefresh')  # time at next scr refresh
                trial3Square.setAutoDraw(False)
        
        # *trial3Fix* updates
        if trial3Fix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial3Fix.frameNStart = frameN  # exact frame index
            trial3Fix.tStart = t  # local t and not account for scr refresh
            trial3Fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3Fix, 'tStartRefresh')  # time at next scr refresh
            trial3Fix.setAutoDraw(True)
        if trial3Fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial3Fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial3Fix.tStop = t  # not accounting for scr refresh
                trial3Fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial3Fix, 'tStopRefresh')  # time at next scr refresh
                trial3Fix.setAutoDraw(False)
        
        # *trial3Resp* updates
        waitOnFlip = False
        if trial3Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial3Resp.frameNStart = frameN  # exact frame index
            trial3Resp.tStart = t  # local t and not account for scr refresh
            trial3Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial3Resp, 'tStartRefresh')  # time at next scr refresh
            trial3Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial3Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial3Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial3Resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial3Resp.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                trial3Resp.tStop = t  # not accounting for scr refresh
                trial3Resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial3Resp, 'tStopRefresh')  # time at next scr refresh
                trial3Resp.status = FINISHED
        if trial3Resp.status == STARTED and not waitOnFlip:
            theseKeys = trial3Resp.getKeys(keyList=['space'], waitRelease=False)
            _trial3Resp_allKeys.extend(theseKeys)
            if len(_trial3Resp_allKeys):
                trial3Resp.keys = _trial3Resp_allKeys[-1].name  # just the last key pressed
                trial3Resp.rt = _trial3Resp_allKeys[-1].rt
                # was this correct?
                if (trial3Resp.keys == str(corrAns)) or (trial3Resp.keys == corrAns):
                    trial3Resp.corr = 1
                else:
                    trial3Resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial3"-------
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials3.addData('trial3Grid.started', trial3Grid.tStartRefresh)
    trials3.addData('trial3Grid.stopped', trial3Grid.tStopRefresh)
    trials3.addData('trial3Square.started', trial3Square.tStartRefresh)
    trials3.addData('trial3Square.stopped', trial3Square.tStopRefresh)
    trials3.addData('trial3Fix.started', trial3Fix.tStartRefresh)
    trials3.addData('trial3Fix.stopped', trial3Fix.tStopRefresh)
    # check responses
    if trial3Resp.keys in ['', [], None]:  # No response was made
        trial3Resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial3Resp.corr = 1;  # correct non-response
        else:
           trial3Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials3 (TrialHandler)
    trials3.addData('trial3Resp.keys',trial3Resp.keys)
    trials3.addData('trial3Resp.corr', trial3Resp.corr)
    if trial3Resp.keys != None:  # we had a response
        trials3.addData('trial3Resp.rt', trial3Resp.rt)
    trials3.addData('trial3Resp.started', trial3Resp.tStartRefresh)
    trials3.addData('trial3Resp.stopped', trial3Resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials3'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
