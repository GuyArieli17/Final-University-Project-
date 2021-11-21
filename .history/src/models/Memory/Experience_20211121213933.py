class Experience:
    def __init__(self,states,actions,rewards,next_states,dones) -> None:
        self.states = states
        self.actions = actions
        self.rewards = rewards
        self.next_states = next_states
        self.dones = dones