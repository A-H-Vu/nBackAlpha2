/******************** 
 * Nbackalpha2 Test *
 ********************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'nBackAlpha2';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructions1RoutineBegin());
flowScheduler.add(instructions1RoutineEachFrame());
flowScheduler.add(instructions1RoutineEnd());
flowScheduler.add(fixation1RoutineBegin());
flowScheduler.add(fixation1RoutineEachFrame());
flowScheduler.add(fixation1RoutineEnd());
const trials1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials1LoopBegin, trials1LoopScheduler);
flowScheduler.add(trials1LoopScheduler);
flowScheduler.add(trials1LoopEnd);
flowScheduler.add(instructions2RoutineBegin());
flowScheduler.add(instructions2RoutineEachFrame());
flowScheduler.add(instructions2RoutineEnd());
flowScheduler.add(fixation2RoutineBegin());
flowScheduler.add(fixation2RoutineEachFrame());
flowScheduler.add(fixation2RoutineEnd());
const trials2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials2LoopBegin, trials2LoopScheduler);
flowScheduler.add(trials2LoopScheduler);
flowScheduler.add(trials2LoopEnd);
flowScheduler.add(instructions3RoutineBegin());
flowScheduler.add(instructions3RoutineEachFrame());
flowScheduler.add(instructions3RoutineEnd());
flowScheduler.add(fixation3RoutineBegin());
flowScheduler.add(fixation3RoutineEachFrame());
flowScheduler.add(fixation3RoutineEnd());
const trials3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials3LoopBegin, trials3LoopScheduler);
flowScheduler.add(trials3LoopScheduler);
flowScheduler.add(trials3LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructions1Clock;
var instr1;
var keyResp1;
var fixation1Clock;
var fix1;
var trial1Clock;
var gridLines1;
var tarSquare1;
var fixTrial1;
var keyRespTrial1;
var instructions2Clock;
var instr2;
var keyResp2;
var fixation2Clock;
var fix2;
var trial2Clock;
var gridLines2;
var tarSquare2;
var fixTrial2;
var keyRespTrial2;
var instructions3Clock;
var instr3;
var keyResp3;
var fixation3Clock;
var fix3;
var trial3Clock;
var gridLines3;
var tarSquare3;
var fixTrial3;
var keyRespTrial3;
var endClock;
var thanks;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions1"
  instructions1Clock = new util.Clock();
  instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr1',
    text: 'In this task you will be required to press space if the white square appeared in the same location as the location on the last trial. For example if the square was in the left down corner on trial 1 and then it appeared in the same location on trial 2, press space. Otherwise, do not respond. Press space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation1"
  fixation1Clock = new util.Clock();
  fix1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial1"
  trial1Clock = new util.Clock();
  gridLines1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'gridLines1', units : undefined, 
    image : 'grid.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  tarSquare1 = new visual.Rect ({
    win: psychoJS.window, name: 'tarSquare1', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fixTrial1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixTrial1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyRespTrial1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions2"
  instructions2Clock = new util.Clock();
  instr2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr2',
    text: 'This is the end of N-back-1 trials. You are about to start N-back-2 trials. This means that instead of pressing space whenever the square appears in the same position as on the position on one trial before, you are required to press space whenever the square appears in the same position as on the position two trials before. For example if the square appeared in left down corner on trial 1, you should press space if the square appears in the left down corner on trial 3. Press space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation2"
  fixation2Clock = new util.Clock();
  fix2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial2"
  trial2Clock = new util.Clock();
  gridLines2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'gridLines2', units : undefined, 
    image : 'grid.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  tarSquare2 = new visual.Rect ({
    win: psychoJS.window, name: 'tarSquare2', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fixTrial2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixTrial2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyRespTrial2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions3"
  instructions3Clock = new util.Clock();
  instr3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr3',
    text: 'This is the end of N-back-2 trials. You are about to start N-back-3 trials. This means that instead of pressing space whenever the square appears in the same position as on the position on one trial before, you are required to press space whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press space if the square appears in the left down corner on trial 4. Press space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation3"
  fixation3Clock = new util.Clock();
  fix3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial3"
  trial3Clock = new util.Clock();
  gridLines3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'gridLines3', units : undefined, 
    image : 'grid.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  tarSquare3 = new visual.Rect ({
    win: psychoJS.window, name: 'tarSquare3', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fixTrial3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixTrial3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  keyRespTrial3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks',
    text: 'This is the end of the experiment.\nThank you for your time.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _keyResp1_allKeys;
var instructions1Components;
function instructions1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instructions1'-------
    t = 0;
    instructions1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp1.keys = undefined;
    keyResp1.rt = undefined;
    _keyResp1_allKeys = [];
    // keep track of which components have finished
    instructions1Components = [];
    instructions1Components.push(instr1);
    instructions1Components.push(keyResp1);
    
    instructions1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instructions1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instructions1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructions1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *keyResp1* updates
    if (t >= 0.0 && keyResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp1.tStart = t;  // (not accounting for frame time here)
      keyResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.clearEvents(); });
    }

    if (keyResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp1.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp1_allKeys = _keyResp1_allKeys.concat(theseKeys);
      if (_keyResp1_allKeys.length > 0) {
        keyResp1.keys = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].name;  // just the last key pressed
        keyResp1.rt = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instructions1'-------
    instructions1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('keyResp1.keys', keyResp1.keys);
    if (typeof keyResp1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp1.rt', keyResp1.rt);
        routineTimer.reset();
        }
    
    keyResp1.stop();
    // the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixation1Components;
function fixation1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'fixation1'-------
    t = 0;
    fixation1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixation1Components = [];
    fixation1Components.push(fix1);
    
    fixation1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function fixation1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'fixation1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixation1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix1* updates
    if (t >= 0.0 && fix1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix1.tStart = t;  // (not accounting for frame time here)
      fix1.frameNStart = frameN;  // exact frame index
      
      fix1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'fixation1'-------
    fixation1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var trials1;
var currentLoop;
function trials1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'nBackCond1.xlsx',
    seed: undefined, name: 'trials1'
  });
  psychoJS.experiment.addLoop(trials1); // add the loop to the experiment
  currentLoop = trials1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials1.forEach(function() {
    const snapshot = trials1.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial1RoutineBegin(snapshot));
    thisScheduler.add(trial1RoutineEachFrame(snapshot));
    thisScheduler.add(trial1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials1LoopEnd() {
  psychoJS.experiment.removeLoop(trials1);

  return Scheduler.Event.NEXT;
}


var trials2;
function trials2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'nBackCond2.xlsx',
    seed: undefined, name: 'trials2'
  });
  psychoJS.experiment.addLoop(trials2); // add the loop to the experiment
  currentLoop = trials2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials2.forEach(function() {
    const snapshot = trials2.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial2RoutineBegin(snapshot));
    thisScheduler.add(trial2RoutineEachFrame(snapshot));
    thisScheduler.add(trial2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials2LoopEnd() {
  psychoJS.experiment.removeLoop(trials2);

  return Scheduler.Event.NEXT;
}


var trials3;
function trials3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'nBackCond3.xlsx',
    seed: undefined, name: 'trials3'
  });
  psychoJS.experiment.addLoop(trials3); // add the loop to the experiment
  currentLoop = trials3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials3.forEach(function() {
    const snapshot = trials3.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial3RoutineBegin(snapshot));
    thisScheduler.add(trial3RoutineEachFrame(snapshot));
    thisScheduler.add(trial3RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials3LoopEnd() {
  psychoJS.experiment.removeLoop(trials3);

  return Scheduler.Event.NEXT;
}


var _keyRespTrial1_allKeys;
var trial1Components;
function trial1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial1'-------
    t = 0;
    trial1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    tarSquare1.setPos([loc1T1, loc2T1]);
    keyRespTrial1.keys = undefined;
    keyRespTrial1.rt = undefined;
    _keyRespTrial1_allKeys = [];
    // keep track of which components have finished
    trial1Components = [];
    trial1Components.push(gridLines1);
    trial1Components.push(tarSquare1);
    trial1Components.push(fixTrial1);
    trial1Components.push(keyRespTrial1);
    
    trial1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trial1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *gridLines1* updates
    if (t >= 0.0 && gridLines1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gridLines1.tStart = t;  // (not accounting for frame time here)
      gridLines1.frameNStart = frameN;  // exact frame index
      
      gridLines1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (gridLines1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      gridLines1.setAutoDraw(false);
    }
    
    // *tarSquare1* updates
    if (t >= 0.0 && tarSquare1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tarSquare1.tStart = t;  // (not accounting for frame time here)
      tarSquare1.frameNStart = frameN;  // exact frame index
      
      tarSquare1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tarSquare1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tarSquare1.setAutoDraw(false);
    }
    
    // *fixTrial1* updates
    if (t >= 1.0 && fixTrial1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixTrial1.tStart = t;  // (not accounting for frame time here)
      fixTrial1.frameNStart = frameN;  // exact frame index
      
      fixTrial1.setAutoDraw(true);
    }

    frameRemains = 1.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixTrial1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixTrial1.setAutoDraw(false);
    }
    
    // *keyRespTrial1* updates
    if (t >= 0.0 && keyRespTrial1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyRespTrial1.tStart = t;  // (not accounting for frame time here)
      keyRespTrial1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyRespTrial1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyRespTrial1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyRespTrial1.clearEvents(); });
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyRespTrial1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyRespTrial1.status = PsychoJS.Status.FINISHED;
  }

    if (keyRespTrial1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyRespTrial1.getKeys({keyList: ['space'], waitRelease: false});
      _keyRespTrial1_allKeys = _keyRespTrial1_allKeys.concat(theseKeys);
      if (_keyRespTrial1_allKeys.length > 0) {
        keyRespTrial1.keys = _keyRespTrial1_allKeys[_keyRespTrial1_allKeys.length - 1].name;  // just the last key pressed
        keyRespTrial1.rt = _keyRespTrial1_allKeys[_keyRespTrial1_allKeys.length - 1].rt;
        // was this correct?
        if (keyRespTrial1.keys == corrAnsT1) {
            keyRespTrial1.corr = 1;
        } else {
            keyRespTrial1.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial1'-------
    trial1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keyRespTrial1.keys === undefined) {
      if (['None','none',undefined].includes(corrAnsT1)) {
         keyRespTrial1.corr = 1;  // correct non-response
      } else {
         keyRespTrial1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyRespTrial1.keys', keyRespTrial1.keys);
    psychoJS.experiment.addData('keyRespTrial1.corr', keyRespTrial1.corr);
    if (typeof keyRespTrial1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyRespTrial1.rt', keyRespTrial1.rt);
        }
    
    keyRespTrial1.stop();
    return Scheduler.Event.NEXT;
  };
}


var _keyResp2_allKeys;
var instructions2Components;
function instructions2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instructions2'-------
    t = 0;
    instructions2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp2.keys = undefined;
    keyResp2.rt = undefined;
    _keyResp2_allKeys = [];
    // keep track of which components have finished
    instructions2Components = [];
    instructions2Components.push(instr2);
    instructions2Components.push(keyResp2);
    
    instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instructions2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instructions2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr2* updates
    if (t >= 0.0 && instr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr2.tStart = t;  // (not accounting for frame time here)
      instr2.frameNStart = frameN;  // exact frame index
      
      instr2.setAutoDraw(true);
    }

    
    // *keyResp2* updates
    if (t >= 0.0 && keyResp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp2.tStart = t;  // (not accounting for frame time here)
      keyResp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp2.clearEvents(); });
    }

    if (keyResp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp2.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp2_allKeys = _keyResp2_allKeys.concat(theseKeys);
      if (_keyResp2_allKeys.length > 0) {
        keyResp2.keys = _keyResp2_allKeys[_keyResp2_allKeys.length - 1].name;  // just the last key pressed
        keyResp2.rt = _keyResp2_allKeys[_keyResp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instructions2'-------
    instructions2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('keyResp2.keys', keyResp2.keys);
    if (typeof keyResp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp2.rt', keyResp2.rt);
        routineTimer.reset();
        }
    
    keyResp2.stop();
    // the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixation2Components;
function fixation2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'fixation2'-------
    t = 0;
    fixation2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixation2Components = [];
    fixation2Components.push(fix2);
    
    fixation2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function fixation2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'fixation2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixation2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix2* updates
    if (t >= 0.0 && fix2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix2.tStart = t;  // (not accounting for frame time here)
      fix2.frameNStart = frameN;  // exact frame index
      
      fix2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'fixation2'-------
    fixation2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _keyRespTrial2_allKeys;
var trial2Components;
function trial2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial2'-------
    t = 0;
    trial2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    tarSquare2.setPos([loc1T2, loc2T2]);
    keyRespTrial2.keys = undefined;
    keyRespTrial2.rt = undefined;
    _keyRespTrial2_allKeys = [];
    // keep track of which components have finished
    trial2Components = [];
    trial2Components.push(gridLines2);
    trial2Components.push(tarSquare2);
    trial2Components.push(fixTrial2);
    trial2Components.push(keyRespTrial2);
    
    trial2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trial2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *gridLines2* updates
    if (t >= 0.0 && gridLines2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gridLines2.tStart = t;  // (not accounting for frame time here)
      gridLines2.frameNStart = frameN;  // exact frame index
      
      gridLines2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (gridLines2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      gridLines2.setAutoDraw(false);
    }
    
    // *tarSquare2* updates
    if (t >= 0.0 && tarSquare2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tarSquare2.tStart = t;  // (not accounting for frame time here)
      tarSquare2.frameNStart = frameN;  // exact frame index
      
      tarSquare2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tarSquare2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tarSquare2.setAutoDraw(false);
    }
    
    // *fixTrial2* updates
    if (t >= 1.0 && fixTrial2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixTrial2.tStart = t;  // (not accounting for frame time here)
      fixTrial2.frameNStart = frameN;  // exact frame index
      
      fixTrial2.setAutoDraw(true);
    }

    frameRemains = 1.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixTrial2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixTrial2.setAutoDraw(false);
    }
    
    // *keyRespTrial2* updates
    if (t >= 0.0 && keyRespTrial2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyRespTrial2.tStart = t;  // (not accounting for frame time here)
      keyRespTrial2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyRespTrial2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyRespTrial2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyRespTrial2.clearEvents(); });
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyRespTrial2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyRespTrial2.status = PsychoJS.Status.FINISHED;
  }

    if (keyRespTrial2.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyRespTrial2.getKeys({keyList: ['space'], waitRelease: false});
      _keyRespTrial2_allKeys = _keyRespTrial2_allKeys.concat(theseKeys);
      if (_keyRespTrial2_allKeys.length > 0) {
        keyRespTrial2.keys = _keyRespTrial2_allKeys[_keyRespTrial2_allKeys.length - 1].name;  // just the last key pressed
        keyRespTrial2.rt = _keyRespTrial2_allKeys[_keyRespTrial2_allKeys.length - 1].rt;
        // was this correct?
        if (keyRespTrial2.keys == corrAnsT2) {
            keyRespTrial2.corr = 1;
        } else {
            keyRespTrial2.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial2'-------
    trial2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keyRespTrial2.keys === undefined) {
      if (['None','none',undefined].includes(corrAnsT2)) {
         keyRespTrial2.corr = 1;  // correct non-response
      } else {
         keyRespTrial2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyRespTrial2.keys', keyRespTrial2.keys);
    psychoJS.experiment.addData('keyRespTrial2.corr', keyRespTrial2.corr);
    if (typeof keyRespTrial2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyRespTrial2.rt', keyRespTrial2.rt);
        }
    
    keyRespTrial2.stop();
    return Scheduler.Event.NEXT;
  };
}


var _keyResp3_allKeys;
var instructions3Components;
function instructions3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instructions3'-------
    t = 0;
    instructions3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp3.keys = undefined;
    keyResp3.rt = undefined;
    _keyResp3_allKeys = [];
    // keep track of which components have finished
    instructions3Components = [];
    instructions3Components.push(instr3);
    instructions3Components.push(keyResp3);
    
    instructions3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instructions3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instructions3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructions3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr3* updates
    if (t >= 0.0 && instr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr3.tStart = t;  // (not accounting for frame time here)
      instr3.frameNStart = frameN;  // exact frame index
      
      instr3.setAutoDraw(true);
    }

    
    // *keyResp3* updates
    if (t >= 0.0 && keyResp3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp3.tStart = t;  // (not accounting for frame time here)
      keyResp3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp3.clearEvents(); });
    }

    if (keyResp3.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp3.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp3_allKeys = _keyResp3_allKeys.concat(theseKeys);
      if (_keyResp3_allKeys.length > 0) {
        keyResp3.keys = _keyResp3_allKeys[_keyResp3_allKeys.length - 1].name;  // just the last key pressed
        keyResp3.rt = _keyResp3_allKeys[_keyResp3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instructions3'-------
    instructions3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('keyResp3.keys', keyResp3.keys);
    if (typeof keyResp3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp3.rt', keyResp3.rt);
        routineTimer.reset();
        }
    
    keyResp3.stop();
    // the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixation3Components;
function fixation3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'fixation3'-------
    t = 0;
    fixation3Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixation3Components = [];
    fixation3Components.push(fix3);
    
    fixation3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function fixation3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'fixation3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixation3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix3* updates
    if (t >= 0.0 && fix3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix3.tStart = t;  // (not accounting for frame time here)
      fix3.frameNStart = frameN;  // exact frame index
      
      fix3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'fixation3'-------
    fixation3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _keyRespTrial3_allKeys;
var trial3Components;
function trial3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial3'-------
    t = 0;
    trial3Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    tarSquare3.setPos([loc1T3, loc2T3]);
    keyRespTrial3.keys = undefined;
    keyRespTrial3.rt = undefined;
    _keyRespTrial3_allKeys = [];
    // keep track of which components have finished
    trial3Components = [];
    trial3Components.push(gridLines3);
    trial3Components.push(tarSquare3);
    trial3Components.push(fixTrial3);
    trial3Components.push(keyRespTrial3);
    
    trial3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trial3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *gridLines3* updates
    if (t >= 0.0 && gridLines3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gridLines3.tStart = t;  // (not accounting for frame time here)
      gridLines3.frameNStart = frameN;  // exact frame index
      
      gridLines3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (gridLines3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      gridLines3.setAutoDraw(false);
    }
    
    // *tarSquare3* updates
    if (t >= 0.0 && tarSquare3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tarSquare3.tStart = t;  // (not accounting for frame time here)
      tarSquare3.frameNStart = frameN;  // exact frame index
      
      tarSquare3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tarSquare3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tarSquare3.setAutoDraw(false);
    }
    
    // *fixTrial3* updates
    if (t >= 1.0 && fixTrial3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixTrial3.tStart = t;  // (not accounting for frame time here)
      fixTrial3.frameNStart = frameN;  // exact frame index
      
      fixTrial3.setAutoDraw(true);
    }

    frameRemains = 1.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixTrial3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixTrial3.setAutoDraw(false);
    }
    
    // *keyRespTrial3* updates
    if (t >= 0.0 && keyRespTrial3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyRespTrial3.tStart = t;  // (not accounting for frame time here)
      keyRespTrial3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyRespTrial3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyRespTrial3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyRespTrial3.clearEvents(); });
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyRespTrial3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyRespTrial3.status = PsychoJS.Status.FINISHED;
  }

    if (keyRespTrial3.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyRespTrial3.getKeys({keyList: ['space'], waitRelease: false});
      _keyRespTrial3_allKeys = _keyRespTrial3_allKeys.concat(theseKeys);
      if (_keyRespTrial3_allKeys.length > 0) {
        keyRespTrial3.keys = _keyRespTrial3_allKeys[_keyRespTrial3_allKeys.length - 1].name;  // just the last key pressed
        keyRespTrial3.rt = _keyRespTrial3_allKeys[_keyRespTrial3_allKeys.length - 1].rt;
        // was this correct?
        if (keyRespTrial3.keys == corrAnsT3) {
            keyRespTrial3.corr = 1;
        } else {
            keyRespTrial3.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial3'-------
    trial3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keyRespTrial3.keys === undefined) {
      if (['None','none',undefined].includes(corrAnsT3)) {
         keyRespTrial3.corr = 1;  // correct non-response
      } else {
         keyRespTrial3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('keyRespTrial3.keys', keyRespTrial3.keys);
    psychoJS.experiment.addData('keyRespTrial3.corr', keyRespTrial3.corr);
    if (typeof keyRespTrial3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyRespTrial3.rt', keyRespTrial3.rt);
        }
    
    keyRespTrial3.stop();
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(thanks);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanks* updates
    if (t >= 0.0 && thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanks.tStart = t;  // (not accounting for frame time here)
      thanks.frameNStart = frameN;  // exact frame index
      
      thanks.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thanks.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
