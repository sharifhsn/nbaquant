from enum import Enum


class ActionType(Enum):
    class Period(Enum):
        START = "Start"
        END = "End"

    class JumpBall(Enum):
        COACH_CHALLENGE = "Coach Challenge"
        OTHER = "Other"

    MADE_SHOT = "Made Shot"
    MISSED_SHOT = "Missed Shot"
    REBOUND = "Rebound"
    FOUL = "Foul"
    TURNOVER = "Turnover"
    TIMEOUT = "Timeout"
    SUBSTITUTION = "Substitution"
    FREE_THROW = "Free Throw"

    class InstantReplay(Enum):
        SUPPORT_RULING = "Support Ruling"
        OVERTURN_RULING = "Overturn Ruling"
        RULING_STANDS = "Ruling Stands"
        COACH_CHALLENGE_SUPPORT_RULING = "Coach Challenge Support Ruling"
        COACH_CHALLENGE_OVERTURN_RULING = "Coach Challenge Overturn Ruling"
        COACH_CHALLENGE_RULING_STANDS = "Coach Challenge Ruling Stands"
        ALTERCATION_RULING = "Altercation Ruling"
        REPLAY_CENTER = "Replay Center"

        def is_coach_challenge(self) -> bool:
            return "Coach Challenge" in self.name

    VIOLATION = "Violation"
    EJECTION = "Ejection"


# action type info

# NaN action type all steals and blocks
# pbp_list[pbp_list["actionType"].isna()]

# action types: period, Jump Ball, Made Shot, Missed Shot, Rebound, Foul, Turnover, Timeout, Substitution, Free Throw, Instant Replay, Instant Reply (trailing spaces), Violation, Foul (trailing spaces), Ejection

# instant replay
# instant replay subtypes: 'Support Ruling', 'Coach Challenge Overturn Ruling', 'Coach Challenge Support Ruling'
# 'Altercation Ruling', 'Overturn Ruling', 'Ruling Stands', 'Coach Challenge Ruling Stands'
# instant replay bunch of spaces, only subtype is 'Replay Center'

# foul
# foul subtypes:
# 'Personal', 'Loose Ball', 'Shooting', 'Offensive', 'Personal Take',
# 'Defense 3 Second', 'Offensive Charge', 'Double Technical',
# 'Flagrant Type 1', 'Technical', 'Away From Play',
# 'Flagrant Type 2', 'Delay Technical', 'Clear Path',
# 'Double Personal', 'Hanging Technical', 'Excess Timeout Technical',
# 'Non-Unsportsmanlike Technical', 'Too Many Players Technical'
# foul with a bunch of spaces: 'Transition Take', 'Flopping', 'Bench'

# period
# period can only be start and end, clock is always 12:00 and 00:00

# jump ball
# jump ball is 'Coach Challenge' or NaN. vast majority are NaN

# made shot and missed shot
# 'Driving Layup Shot', 'Driving Finger Roll Layup Shot',
#        'Alley Oop Dunk Shot', 'Running Layup Shot', 'Jump Shot',
#        'Pullup Jump shot', 'Driving Floating Bank Jump Shot',
#        'Fadeaway Jump Shot', 'Cutting Dunk Shot',
#        'Running Reverse Layup Shot', 'Driving Floating Jump Shot',
#        'Cutting Finger Roll Layup Shot', 'Cutting Layup Shot',
#        'Turnaround Fadeaway shot', 'Dunk Shot', 'Step Back Jump shot',
#        'Putback Layup Shot', 'Running Jump Shot', 'Fadeaway Bank shot',
#        'Tip Dunk Shot', 'Layup Shot', 'Running Alley Oop Dunk Shot',
#        'Floating Jump shot', 'Driving Hook Shot', 'Tip Layup Shot',
#        'Jump Bank Shot', 'Running Pull-Up Jump Shot', 'Driving Dunk Shot',
#        'Driving Reverse Layup Shot', 'Running Dunk Shot',
#        'Putback Dunk Shot', 'Turnaround Jump Shot', 'Reverse Layup Shot',
#        'Turnaround Hook Shot', 'Turnaround Fadeaway Bank Jump Shot',
#        'Hook Shot', 'Driving Bank Hook Shot', 'Turnaround Bank Hook Shot',
#        'Reverse Dunk Shot', 'Turnaround Bank shot',
#        'Alley Oop Layup shot', 'Running Finger Roll Layup Shot',
#        'Step Back Bank Jump Shot', 'Hook Bank Shot',
#        'Running Alley Oop Layup Shot', 'Finger Roll Layup Shot',
#        'Driving Reverse Dunk Shot', 'Running Reverse Dunk Shot'

# Rebound
# either Unknown or "Normal Rebound" or "Dead Ball Rebound" (extremely rare), vast majority are Unknown
# TODO: differentiate these into offensive, defensive, more?
# for Unknown, some of them have the description of who did the rebound
# others just say the team that did the rebound and everything else is NaN. TODO: look into why this is?

# turnover
# 'Lost Ball', 'Offensive Foul Turnover', 'Bad Pass',
#        'Out of Bounds - Bad Pass Turnover', 'Traveling',
#        'Out of Bounds Lost Ball Turnover', 'Shot Clock Turnover',
#        'Step Out of Bounds Turnover', 'Double Dribble',
#        'Backcourt Turnover', 'Offensive Goaltending', 'Lane Violation',
#        '3 Second Violation', '5 Second Violation',
#        'Kicked Ball Violation', 'Palming Turnover', '8 Second Violation',
#        'Inbound Turnover', 'Illegal Assist Turnover',
#        'Jump Ball Violation', 'Discontinue Dribble',
#        'Illegal Screen Turnover', 'Punched Ball Turnover',
#        'Excess Timeout Turnover', 'Basket from Below Turnover',
#        'Swinging Elbows Turnover', '10 Second Violaton'

# timeout
# vast majority are 'Regular', few are 'Coach Challenge'

# substitution has no subtypes

# free throws
# 'Free Throw 1 of 1', 'Free Throw 1 of 2', 'Free Throw 2 of 2',
#        'Free Throw 1 of 3', 'Free Throw 2 of 3', 'Free Throw 3 of 3',
#        'Free Throw Technical', 'Free Throw Flagrant 1 of 2',
#        'Free Throw Flagrant 2 of 2', 'Free Throw Flagrant 1 of 3',
#        'Free Throw Flagrant 2 of 3', 'Free Throw Flagrant 3 of 3',
#        'Free Throw Flagrant 1 of 1', 'Free Throw Clear Path 1 of 2',
#        'Free Throw Clear Path 2 of 2', 'Free Throw Technical 1 of 2',
#        'Free Throw Technical 2 of 2'

# violation
# 'Lane', 'Defensive Goaltending', 'Kicked Ball', 'Delay Of Game',
#        'Double Lane', 'Jump Ball'

# ejection
# "First Flagrant Type 2", "Second Flagrant Type 1" (rare) "Second Technical" "Other" (vast majority)
# ejection with a bunch of spaces is a non-player ejection like Poppovich or some other type not covered

# pbp_list["actionType"].unique()
# pbp_list[pbp_list["actionType"] == "Jump Ball"]["subType"].value_counts() #["subType"].value_counts() #["actionType"].value_counts() #["subType"].value_counts()
# games_list[games_list["GAME_ID"] == "0021400465"]
# pbp_list[pbp_list["gameId"]]
