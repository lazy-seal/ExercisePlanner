

# constants
DefaultReps = 10
DefaultSets = 3
DefaultRest = 1


class Exercise:
    """Individual exercise with related info"""
    def __init__(self):
        def typecastingAlternateNames() -> list[str]:
            """To type cast list of strings of alternate names for exercises"""
            return []
        self.name = ""      # name of the exercise
        self.alternate_names = typecastingAlternateNames()        # alternate names for the exercise
        self.instruction = ""       # instruction for the exercise
        self.notes = ""     # notes for the exercise


class ExerciseRecord:
    """Records of an exercise with 수행정보 (reps, sets, etc.)"""
    def __init__(self, exercise: Exercise):
        self.exercise = exercise        # exercise object
        self.reps = DefaultReps       # repetition per set
        self.sets = DefaultSets       # sets
        self.rest = DefaultRest       # rests between set in minutes
        self.notes = ""     # notes for the exercise


class DailyRoutine:
    """Daily lists of records of exercise that have been or will be executed"""
    def __init__(self):
        def typecastingRecords() -> list[ExerciseRecord]:
            return []
        self.records = typecastingRecords()     # all records of the exercise