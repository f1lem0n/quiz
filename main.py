#!/usr/bin/env python3

import random as r
import sys

with open('pytaniaOWI.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        lines[idx] = line.strip('\n')

    Q = []
    while lines:
        Q.append(lines[:4])
        lines = lines[4:]

A = 'bcabacbababcabcbbcababcababcabcabacabcaabcbacabcbacababbbcacbababcabacbabaabcaababcabacbacbcabbabababacaacabcaaaacbababacbabcababbacbcabaababbbcababcabbcaabacab'
asked = []


def ask(n, Q):
    q_num = r.randint(0, n)
    if q_num not in asked:
        for line in Q[q_num]:
            print(line)
        answer = input('Podaj odpowiedź (a/b/c): ').lower()
    return q_num, answer


def check_answer(q_num, answer, A):
    if answer == A[q_num]:
        return True, A[q_num]
    else:
        return False, A[q_num]


while True:
    q_num, answer = ask(160, Q)
    asked.append(q_num)
    verdict, correct = check_answer(q_num, answer, A)
    if verdict:
        print('Gooooood, Anakin, good...')
    else:
        print('YOU WERE SUPPOSE TO DESTROY THE SITH NOT JOIN THEM!')
        print(f'Prawidłowa odpowiedź to: {correct}')
    if input('Type any key to continue\nType q to exit\n') in ('q', 'Q'):
        sys.exit()
    else:
        continue
