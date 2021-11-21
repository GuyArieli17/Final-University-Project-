class Experience:
    def __init__(self,states,rewards,next_states,dones) -> None:
        self.states = states
        self.rewards = rewards
        self.next_states = next_states
        self.dones = dones