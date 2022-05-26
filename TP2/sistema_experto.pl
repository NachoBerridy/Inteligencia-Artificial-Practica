/*Axiomas*/

verificar(thickness_less_than_threshold_limit):-
                estado(thickness_less_than_threshold_limit, yes), writeln('equipment status will be reported to the Technical Ispection Unit immedialety').
verificar(thickness_less_than_threshold_limit):-                
                estado(thickness_less_than_threshold_limit, no), writeln('The condicion of the equipment is suitable').
verificar(thickness_less_than_threshold_limit):-                
                estado(thickness_less_than_threshold_limit, desconocido), verificar(safety_valve_body_pipe_and_joints_having_dazzling_rusting).


verificar(safety_valve_body_pipe_and_joints_having_dazzling_rusting):-
                estado(safety_valve_body_pipe_and_joints_having_dazzling_rusting, yes), writeln('Coordination is required in order to render and color the equipment').
verificar(safety_valve_body_pipe_and_joints_having_dazzling_rusting):-
                estado(safety_valve_body_pipe_and_joints_having_dazzling_rusting, no), writeln('Verificar thickness').
verificar(safety_valve_body_pipe_and_joints_having_dazzling_rusting):-
                estado(safety_valve_body_pipe_and_joints_having_dazzling_rusting, desconocido), writeln('Verificar the safety valve body, pipes and joins').




                
verificar(piloto) :-
                estado(pilot, yes), writeln('Set the safety valve according to the instructions').
verificar(piloto) :-
                estado(pilot, no), writeln('Pilot full service and reinstallation').
verificar(piloto) :-
                estado(pilot, desconocido), verificar(leakage_prevention_between_sit_and_orifice).

                
verificar(leakage_prevention_between_sit_and_orifice) :-
                estado(leakage_prevention_between_sit_and_orifice, yes), writeln('Verificar piloto').
verificar(leakage_prevention_between_sit_and_orifice) :-
                estado(leakage_prevention_between_sit_and_orifice, no), writeln('Replace Sit and Orifice and put the safety valve into circuit').
verificar(leakage_prevention_between_sit_and_orifice) :-
                estado(leakage_prevention_between_sit_and_orifice, desconocido), verificar(safety_valve_spring).

                
verificar(safety_valve_spring) :-
                estado(safety_valve_spring, yes), writeln('Verificar leakage prevention between sit and orifice').
verificar(safety_valve_spring) :-
                estado(safety_valve_spring, no), writeln('Putting spring and safety in the service').
verificar(safety_valve_spring) :-
                estado(safety_valve_spring, desconocido), verificar(control_valve_blocked).


verificar(control_valve_blocked) :-
                estado(control_valve_blocked, yes), writeln('Cleaning troubleshooting of the sensing pipes').
verificar(control_valve_blocked) :-
                estado(control_valve_blocked, no), writeln('verificar safety valve spring').
verificar(control_valve_blocked) :-
                estado(control_valve_blocked, desconocido), verificar(valve_status_closed).


verificar(valve_status_closed) :-
                estado(valve_status_closed, yes), writeln('Place the safety valve in open poition').
verificar(valve_status_closed) :-
                estado(valve_status_closed, no), writeln('Verificar control valve blocked').
verificar(valve_status_closed) :-
                estado(valve_status_closed, desconocido), verificar(relief_valve_ok_with_10_percent_more_pressure).
                

verificar(relief_valve_ok_with_10_percent_more_pressure) :-
                estado(relief_valve_ok_with_10_percent_more_pressure, yes), writeln('Safety function is appropriate').
verificar(relief_valve_ok_with_10_percent_more_pressure) :-
                estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Verificar valve status closed').
verificar(relief_valve_ok_with_10_percent_more_pressure) :-
                estado(relief_valve_ok_with_10_percent_more_pressure, desconocido), verificar(safety_valve_has_continuous_evacuation).


verificar(preventable_leakage_between_sit_and_orifice) :-
                estado(preventable_leakage_between_sit_and_orifice, yes), writeln('Set the safety valve according to thr instructions').
verificar(preventable_leakage_between_sit_and_orifice) :-
                estado(preventable_leakage_between_sit_and_orifice, no), writeln('Replace Sit and Orifice and put the valve into circuit').
verificar(preventable_leakage_between_sit_and_orifice) :-
                estado(preventable_leakage_between_sit_and_orifice, desconocido), verificar(safety_spring_effective).
                
                
verificar(safety_spring_effective) :-
                estado(safety_spring_effective, yes), writeln('Verificar preventable leakage between sit and orifice').
verificar(safety_spring_effective) :-
                estado(safety_spring_effective, no), writeln('Replace the safety spring in the service').                
verificar(safety_spring_effective) :-
                estado(safety_spring_effective, desconocido), verificar(control_and_pressure_sensor_pipes_blocked).


verificar(control_and_pressure_sensor_pipes_blocked) :-
                estado(control_and_pressure_sensor_pipes_blocked, yes), writeln('Clean up and fix the faults of the sensing pipes').
verificar(control_and_pressure_sensor_pipes_blocked) :-
                estado(control_and_pressure_sensor_pipes_blocked, no), writeln('Verificar safety spring').
verificar(control_and_pressure_sensor_pipes_blocked) :-
                estado(control_and_pressure_sensor_pipes_blocked, desconocido),verificar(gas_pressure_appropriate).


verificar(gas_pressure_appropriate) :-
                estado(gas_pressure_appropriate, yes), writeln('Verificar control and pressure sensor pipes').                
verificar(gas_pressure_appropriate) :-
                estado(gas_pressure_appropriate, no), writeln(' Adjust the regulator acording to the instruccion').
verificar(gas_pressure_appropriate) :-
                estado(gas_pressure_appropriate, desconocido), verificar(safety_valve_has_continuous_evacuation).


verificar(safety_valve_has_continuous_evacuation) :-
                estado(safety_valve_has_continuous_evacuation, yes), writeln('Verificar gas pressure appropriate').             
verificar(safety_valve_has_continuous_evacuation) :-
                estado(safety_valve_has_continuous_evacuation, no), writeln('Verificar relief valve ok with 10 percent more pressure').             
verificar(safety_valve_has_continuous_evacuation) :-
                estado(safety_valve_has_continuous_evacuation, desconocido), writeln('Verificar safety valve has a continuous evacuation').





verificar(leakage_fixed_with_wrench_joints) :-
                estado(leakage_fixed_with_wrench_joints, yes), writeln('Report to Technical Inspection Unit').
verificar(leakage_fixed_with_wrench_joints) :-
                estado(leakage_fixed_with_wrench_joints, no), writeln('Send a report to the repair department to fix the fault').
verificar(leakage_fixed_with_wrench_joints) :-
                estado(leakage_fixed_with_wrench_joints, desconocido), verificar(gas_leakage_at_joint).


verificar(gas_leakage_at_joint):-
                estado(gas_leakage_at_joint, yes), writeln('Verificar leakage fixed with the wrench at joints ').
verificar(gas_leakage_at_joint):-
                estado(gas_leakage_at_joint, no), writeln('The safety valve joint are free of gas leakage').
verificar(gas_leakage_at_joint):-
                estado(gas_leakage_at_joint, desconocido), writeln('Verificar gas leakage at joint').



             

                
/*Ground Facts*/


estado(safety_valve_body_pipe_and_joints_having_dazzling_rusting, desconocido).
estado(thickness_less_than_threshold_limit, desconocido).

estado(safety_valve_has_continuous_evacuation, no).

estado(relief_valve_ok_with_10_percent_more_pressure, yes).
estado(valve_status_closed, desconocido).
estado(control_valve_blocked, desconocido).
estado(safety_valve_spring, desconocido).
estado(leakage_prevention_between_sit_and_orifice, desconocido).
estado(pilot, desconocido).

estado(gas_pressure_appropriate, desconocido).
estado(control_and_pressure_sensor_pipes_blocked, desconocido).
estado(safety_spring_effective, desconocido).
estado(preventable_leakage_between_sit_and_orifice, desconocido).

estado(gas_leakage_at_joint, desconocido).
estado(leakage_fixed_with_wrench_joints, desconocido).