# -------------------------------------
# handling good choices with event handlers, too
# -------------------------------------

answer()

ask("Hi. For sales, say sales or press 1. For support, say support or press 2", 
{'choices':"sales(1,sales), support(2,support)", 'repeat':3, 
'onBadChoice': lambda : say("I'm sorry, I didn't understand what you said."),
'onTimeout': lambda : say("I'm sorry. I didn't hear anything."),
'onChoices' : lambda event:
      event.onChoice( "sales", lambda : say("Ok, let me transfer you to sales" ) and transfer("14075551111")) and
      event.onChoice( "support", lambda : say("Ok, let me transfer you to support") and transfer("14075552222") )
})