# my_states.py

from State import State

# Start of our states
class NoAssignmentState(State):
    """
    The state which indicates that there are limited device capabilities.
    """
    def on_event(self, event):
        if event == 'Assignment Received':
            return WorkingState()

        return self

class WorkingState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'Working':
            return CompletedState()

        return self

class CompletedState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'Completed':
            return ReviewedState()

        return self

class ReviewedState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'Reviewed':
            return NoAssignmentState()
        elif event == 'Feedback':
            return WorkingState()

        return self