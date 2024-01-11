#!/usr/bin/env python3

# Free motion 상태에서 모터 토크 값을 csv 파일로 저장하는 코드

import os
from mujoco_py import load_model_from_path, MjSim, MjViewer
import csv
import time
 
model = load_model_from_path("/home/robros/model_uncertainty/model/gen3lite.xml")
 
# Simulation Setup
sim = MjSim(model)
viewer = MjViewer(sim)
 
joint_names = ['J0', 'J1', 'J2', 'J3', 'J4']
joint_indices = [model.joint_names.index(name) for name in joint_names]
 
# CSV 파일 설정
csv_filename = "../csv/joint_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    headers = ["Time"] + [f"P_{name}" for name in joint_names] + [f"V_{name}" for name in joint_names] + [f"A_{name}" for name in joint_names]
    writer.writerow(headers)
 
    # Start Simulation
    start_time = time.time()
    prev_velocities = [0] * len(joint_names)
    while True:
        current_time = time.time() - start_time
        sim.step()
        viewer.render()
 
        # 관절 위치 변경
        for i in joint_indices:
            sim.data.qpos[i] += 0.001
 
        # 각 관절의 위치, 속도 기록
        joint_positions = [sim.data.qpos[idx] for idx in joint_indices]
        joint_velocities = [sim.data.qvel[idx] for idx in joint_indices]
        # 가속도 계산
        dt = current_time - (prev_time if 'prev_time' in locals() else 0)
        joint_accelerations = [(v - pv) / dt if dt > 0 else 0 for v, pv in zip(joint_velocities, prev_velocities)]
 
        # 데이터 기록
        writer.writerow([current_time] + joint_positions + joint_velocities + joint_accelerations)
 
        # 이전 값 업데이트
        prev_time = current_time
        prev_velocities = joint_velocities
 
        # 시뮬레이션 종료 조건
        if current_time > 10:  # 10초 후에 종료
            break