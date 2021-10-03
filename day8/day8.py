#!/usr/bin/env python3

# https://adventofcode.com/2020/day/8

import re
from enum import Enum


class Observable(object):
    def __init__(self):
        self.callbacks = []
    def subscribe(self, callback):
        self.callbacks.append(callback)
    def fire(self, **kwargs):
        for fn in self.callbacks:
            fn(**kwargs)

def parse(s):
    return Instruction.parse(s)

def load_data(filename) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            data.append(parse(line.strip()))
    return data


class OpCode(Enum):
    acc = 1
    jmp = 2
    nop = 0

class Instruction:
    def __init__(self, opcode: OpCode, value: int):
        self.opcode = opcode
        self.value = value

    def __repr__(self):

        return f"{self.opcode.name} {self.value}";

    @classmethod
    def parse(cls, s: str):
        pattern = ''.join([
            "([a-z ]*)\s"  # opcode
            "([+-][\d]*)", # numeric value
        ])
        m = re.search(pattern, s)
        if m != None:
            # print(f"Parsed: {m.group(1)}, {m.group(2)}")
            valid_opcodes = list(map(lambda op: op.name, OpCode))
            if m.group(1) in valid_opcodes:
                return Instruction(OpCode[m.group(1)], int(m.group(2)))

        raise Exception(f"invalid program instruction: {s}")    


class Processor:
    def __init__(self, instructions: [Instruction]):
        self.SP = 0
        self.ACC = 0
        self.instructions = instructions
        self.process_instruction_observable = Observable()

    def run(self):
        try:
            while self.SP < len(self.instructions):
                instruction = self.instructions[self.SP]
                self.process_instruction(instruction)
        except Exception as e:
           print(e)

    def process_instruction(self, instruction):
        # print(f"{self.SP}: {instruction}")
        self.process_instruction_observable.fire(processor = self)
        if instruction.opcode == OpCode.nop:
            pass
        if instruction.opcode == OpCode.acc:
            self.ACC += instruction.value
        if instruction.opcode == OpCode.jmp:
            self.SP += instruction.value    
        else:
            self.SP += 1        


class DetectInfiniteLoop:
    def __init__(self, processor: Processor):
        # allocate a array for length of all instructions
        self.run_instructions = [False] * len(processor.instructions)
        processor.process_instruction_observable.subscribe(self.observe_instruction)

    def observe_instruction(self, processor: Processor):
        if self.run_instructions[processor.SP] == True:
            raise Exception(f"Infinite loop detected. Acc={processor.ACC}") 
        self.run_instructions[processor.SP] = True


def main():
    data = load_data('input.txt')
    # print(data)

    processor = Processor(data)
    # add in a processor observer to detect running same instruction
    detector = DetectInfiniteLoop(processor)
    processor.run()

if __name__ == "__main__":
    main()
