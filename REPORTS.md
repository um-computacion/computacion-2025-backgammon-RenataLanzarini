# 📊 Reporte de Tests y Cobertura

**Fecha:** 2025-10-31 22:37:07
**Branch:** 98-ultimas-correcciones
**Commit:** f2ecdbf8
**Autor:** RenataLanzarini

---

## �� Resultados de Tests

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.3, pluggy-1.6.0 -- /home/renata/repos/computacion-2025-backgammon-RenataLanzarini/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/renata/repos/computacion-2025-backgammon-RenataLanzarini
configfile: pytest.ini
testpaths: tests
plugins: mock-3.12.0, cov-4.1.0
collecting ... collected 292 items

tests/test_board.py::test_tablero_inicia_sin_fichas_y_con_24_puntos PASSED [  0%]
tests/test_board.py::test_colocar_y_quitar_ficha PASSED                  [  0%]
tests/test_board.py::test_representacion_str PASSED                      [  1%]
tests/test_board.py::test_punto_valido PASSED                            [  1%]
tests/test_board.py::test_tablero_vacio PASSED                           [  1%]
tests/test_board.py::test_limpiar_punto PASSED                           [  2%]
tests/test_board.py::test_total_puntos PASSED                            [  2%]
tests/test_board.py::test_mover_ficha PASSED                             [  2%]
tests/test_board.py::test_mover_ficha_error PASSED                       [  3%]
tests/test_board.py::test_colocar_ficha_invalida PASSED                  [  3%]
tests/test_board.py::test_reset_con_fichas PASSED                        [  3%]
tests/test_board.py::test_ficha_en_punto_vacio PASSED                    [  4%]
tests/test_board.py::test_quitar_ficha_vacia PASSED                      [  4%]
tests/test_board.py::test_configurar_inicial PASSED                      [  4%]
tests/test_board.py::test_configurar_inicial_fichas_x PASSED             [  5%]
tests/test_board.py::test_configurar_inicial_fichas_o PASSED             [  5%]
tests/test_board.py::test_configurar_inicial_posiciones PASSED           [  5%]
tests/test_board.py::test_contar_fichas_jugador PASSED                   [  6%]
tests/test_board.py::test_barra_inicialmente_vacia PASSED                [  6%]
tests/test_board.py::test_capturar_ficha_x PASSED                        [  6%]
tests/test_board.py::test_capturar_ficha_o PASSED                        [  7%]
tests/test_board.py::test_tiene_fichas_en_barra PASSED                   [  7%]
tests/test_board.py::test_sacar_de_barra PASSED                          [  7%]
tests/test_board.py::test_fichas_en_barra PASSED                         [  8%]
tests/test_cli.py::test_cli_iniciar_muestra_mensaje PASSED               [  8%]
tests/test_cli.py::test_cli_comando_estado PASSED                        [  8%]
tests/test_cli.py::test_cli_comando_reiniciar PASSED                     [  9%]
tests/test_cli.py::test_cli_comando_tirar PASSED                         [  9%]
tests/test_cli.py::test_cli_comando_tablero PASSED                       [  9%]
tests/test_cli.py::test_cli_comando_ayuda PASSED                         [ 10%]
tests/test_cli.py::test_cli_comando_desconocido PASSED                   [ 10%]
tests/test_cli.py::test_mostrar_estado PASSED                            [ 10%]
tests/test_cli.py::test_reiniciar_juego PASSED                           [ 11%]
tests/test_cli.py::test_salir PASSED                                     [ 11%]
tests/test_cli.py::test_mostrar_tablero_vacio PASSED                     [ 11%]
tests/test_cli.py::test_mostrar_ayuda PASSED                             [ 12%]
tests/test_cli.py::test_mostrar_bienvenida PASSED                        [ 12%]
tests/test_cli.py::test_formato_barra_sin_fichas PASSED                  [ 13%]
tests/test_cli.py::test_cli_ejecuta_sin_errores PASSED                   [ 13%]
tests/test_cli.py::test_mostrar_tablero_con_texto PASSED                 [ 13%]
tests/test_cli.py::test_cli_comando_mover_con_tablero PASSED             [ 14%]
tests/test_cli.py::test_mostrar_victoria PASSED                          [ 14%]
tests/test_cli.py::test_cli_comando_help_alias PASSED                    [ 14%]
tests/test_cli.py::test_cli_comando_h_alias PASSED                       [ 15%]
tests/test_cli.py::test_cli_comando_question_alias PASSED                [ 15%]
tests/test_cli.py::test_cli_comando_exit_alias PASSED                    [ 15%]
tests/test_cli.py::test_cli_comando_q_alias PASSED                       [ 16%]
tests/test_cli.py::test_cli_entrada_vacia PASSED                         [ 16%]
tests/test_cli.py::test_mostrar_victoria_jugador_o PASSED                [ 16%]
tests/test_cli.py::test_formato_barra_cero_fichas PASSED                 [ 17%]
tests/test_cli.py::test_cli_init PASSED                                  [ 17%]
tests/test_cli.py::test_procesar_tirada_valida PASSED                    [ 17%]
tests/test_cli.py::test_procesar_tirada_con_ganador PASSED               [ 18%]
tests/test_cli.py::test_visualizacion_puntos PASSED                      [ 18%]
tests/test_cli.py::test_metodos_existentes PASSED                        [ 18%]
tests/test_cli.py::test_comandos_aliases PASSED                          [ 19%]
tests/test_cli.py::test_mostrar_estado_detallado PASSED                  [ 19%]
tests/test_cli.py::test_reiniciar_con_juego PASSED                       [ 19%]
tests/test_cli.py::test_manejo_excepciones PASSED                        [ 20%]
tests/test_cli.py::test_flujo_completo_basico PASSED                     [ 20%]
tests/test_cli.py::test_formato_barra_varios_casos PASSED                [ 20%]
tests/test_cli.py::test_mostrar_victoria_varios_casos PASSED             [ 21%]
tests/test_cli.py::test_posibles_metodos_privados PASSED                 [ 21%]
tests/test_cli.py::test_rendimiento_metodos_basicos PASSED               [ 21%]
tests/test_cli.py::test_llamadas_repetidas PASSED                        [ 22%]
tests/test_cli.py::test_diferentes_casos_formato_barra PASSED            [ 22%]
tests/test_cli.py::test_multiples_comandos PASSED                        [ 22%]
tests/test_cli.py::test_metodos_sin_parametros PASSED                    [ 23%]
tests/test_cli.py::test_cobertura_formato_barra_con_fichas PASSED        [ 23%]
tests/test_cli.py::test_cobertura_explicar_error PASSED                  [ 23%]
tests/test_cli.py::test_cobertura_sugerencias_sin_barra PASSED           [ 24%]
tests/test_cli.py::test_cobertura_sugerencias_con_barra PASSED           [ 24%]
tests/test_cli.py::test_cobertura_toggle_tutorial PASSED                 [ 25%]
tests/test_cli.py::test_cobertura_tirar_con_dados_disponibles PASSED     [ 25%]
tests/test_cli.py::test_cobertura_obtener_simbolo PASSED                 [ 25%]
tests/test_cli.py::test_cobertura_mostrar_info_barra PASSED              [ 26%]
tests/test_cli.py::test_cobertura_mostrar_dados_con_ayuda PASSED         [ 26%]
tests/test_cli.py::test_cobertura_procesar_movimiento PASSED             [ 26%]
tests/test_cli.py::test_cobertura_procesar_movimiento_invalido PASSED    [ 27%]
tests/test_cli.py::test_cobertura_procesar_movimiento_sin_params PASSED  [ 27%]
tests/test_cli.py::test_cobertura_mostrar_fichas_fuera PASSED            [ 27%]
tests/test_cli.py::test_procesar_pasar_turno_sin_dados PASSED            [ 28%]
tests/test_cli.py::test_procesar_pasar_turno_con_ganador PASSED          [ 28%]
tests/test_cli.py::test_procesar_pasar_turno_con_movimientos PASSED      [ 28%]
tests/test_cli.py::test_comando_pasar_en_flujo PASSED                    [ 29%]
tests/test_cli.py::test_procesar_pasar_turno_sin_movimientos_barra PASSED [ 29%]
tests/test_cli.py::test_procesar_pasar_turno_sin_movimientos_normales PASSED [ 29%]
tests/test_cli.py::test_ayuda_contiene_pasar PASSED                      [ 30%]
tests/test_cli.py::test_comando_pasar_directo PASSED                     [ 30%]
tests/test_cli.py::test_mostrar_fichas_fuera_con_capsys PASSED           [ 30%]
tests/test_dice.py::test_valor_en_rango PASSED                           [ 31%]
tests/test_dice.py::test_dobles PASSED                                   [ 31%]
tests/test_dice.py::test_tirar_devuelve_lista PASSED                     [ 31%]
tests/test_dice.py::test_valores_property PASSED                         [ 32%]
tests/test_game.py::TestEstadosDelJuego::test_estado_inicial PASSED      [ 32%]
tests/test_game.py::TestEstadosDelJuego::test_iniciar_cambia_estado PASSED [ 32%]
tests/test_game.py::TestEstadosDelJuego::test_pausar_cambia_estado PASSED [ 33%]
tests/test_game.py::TestEstadosDelJuego::test_finalizar_cambia_estado PASSED [ 33%]
tests/test_game.py::TestEstadosDelJuego::test_reiniciar PASSED           [ 33%]
tests/test_game.py::TestPropiedades::test_propiedad_estado PASSED        [ 34%]
tests/test_game.py::TestPropiedades::test_propiedad_turno PASSED         [ 34%]
tests/test_game.py::TestPropiedades::test_propiedad_tablero PASSED       [ 34%]
tests/test_game.py::TestPropiedades::test_propiedad_jugadores PASSED     [ 35%]
tests/test_game.py::TestPropiedades::test_propiedad_dados PASSED         [ 35%]
tests/test_game.py::TestPropiedades::test_propiedad_dados_disponibles PASSED [ 35%]
tests/test_game.py::TestTurnos::test_cambiar_turno PASSED                [ 36%]
tests/test_game.py::TestTurnos::test_cambiar_turno_limpia_dados PASSED   [ 36%]
tests/test_game.py::TestTurnos::test_jugador_actual PASSED               [ 36%]
tests/test_game.py::TestDados::test_tirar_dados PASSED                   [ 37%]
tests/test_game.py::TestDados::test_tirar_dados_actualiza_disponibles PASSED [ 37%]
tests/test_game.py::TestDados::test_tiene_dados_disponibles_true PASSED  [ 38%]
tests/test_game.py::TestDados::test_tiene_dados_disponibles_false PASSED [ 38%]
tests/test_game.py::TestDescripcion::test_descripcion_formato PASSED     [ 38%]
tests/test_game.py::TestDescripcion::test_descripcion_jugador_1 PASSED   [ 39%]
tests/test_game.py::TestDescripcion::test_descripcion_jugador_2 PASSED   [ 39%]
tests/test_game.py::TestMovimientosBasicos::test_movimientos_disponibles PASSED [ 39%]
tests/test_game.py::TestMovimientosBasicos::test_colocar_ficha_punto_valido PASSED [ 40%]
tests/test_game.py::TestMovimientosBasicos::test_colocar_ficha_punto_invalido PASSED [ 40%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_valido_jugador_x PASSED [ 40%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_valido_jugador_o PASSED [ 41%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_sin_dados PASSED [ 41%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_origen_invalido PASSED [ 41%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_destino_invalido PASSED [ 42%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_origen_vacio PASSED [ 42%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_ficha_incorrecta PASSED [ 42%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_distancia_incorrecta PASSED [ 43%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_distancia_negativa PASSED [ 43%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_bloqueado_dos_fichas PASSED [ 43%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_bloqueado_mas_de_dos_fichas PASSED [ 44%]
tests/test_game.py::TestValidacionMovimientos::test_movimiento_sobre_ficha_propia PASSED [ 44%]
tests/test_game.py::TestAplicarMovimientos::test_aplicar_movimiento_exitoso PASSED [ 44%]
tests/test_game.py::TestAplicarMovimientos::test_aplicar_movimiento_invalido PASSED [ 45%]
tests/test_game.py::TestAplicarMovimientos::test_aplicar_movimiento_consume_dado PASSED [ 45%]
tests/test_game.py::TestAplicarMovimientos::test_aplicar_varios_movimientos PASSED [ 45%]
tests/test_game.py::TestAplicarMovimientos::test_aplicar_movimiento_con_dobles PASSED [ 46%]
tests/test_game.py::TestCaptura::test_captura_ficha_enemiga PASSED       [ 46%]
tests/test_game.py::TestCaptura::test_captura_no_ocurre_con_ficha_propia PASSED [ 46%]
tests/test_game.py::TestBarra::test_puede_reingresar_desde_barra_x PASSED [ 47%]
tests/test_game.py::TestBarra::test_puede_reingresar_desde_barra_o PASSED [ 47%]
tests/test_game.py::TestBarra::test_no_puede_reingresar_sin_fichas_en_barra PASSED [ 47%]
tests/test_game.py::TestBarra::test_no_puede_reingresar_sin_dado_correcto PASSED [ 48%]
tests/test_game.py::TestBarra::test_no_puede_reingresar_punto_bloqueado PASSED [ 48%]
tests/test_game.py::TestBarra::test_puede_reingresar_punto_con_una_ficha_enemiga PASSED [ 48%]
tests/test_game.py::TestBarra::test_reingreso_desde_barra_exitoso PASSED [ 49%]
tests/test_game.py::TestBarra::test_reingreso_con_captura PASSED         [ 49%]
tests/test_game.py::TestBarra::test_debe_reingresar_antes_de_mover PASSED [ 50%]
tests/test_game.py::TestBarra::test_obtener_movimientos_validos_desde_barra_x PASSED [ 50%]
tests/test_game.py::TestBarra::test_obtener_movimientos_validos_desde_barra_o PASSED [ 50%]
tests/test_game.py::TestBarra::test_obtener_movimientos_desde_barra_sin_fichas PASSED [ 51%]
tests/test_game.py::TestBarra::test_obtener_movimientos_desde_barra_jugador_incorrecto PASSED [ 51%]
tests/test_game.py::TestBarra::test_reingreso_x_fuera_de_home_board PASSED [ 51%]
tests/test_game.py::TestBarra::test_reingreso_o_fuera_de_home_board PASSED [ 52%]
tests/test_game.py::TestGanadores::test_verificar_ganador_sin_ganador PASSED [ 52%]
tests/test_game.py::TestGanadores::test_verificar_ganador_x_gana PASSED  [ 52%]
tests/test_game.py::TestGanadores::test_verificar_ganador_o_gana PASSED  [ 53%]
tests/test_game.py::TestGanadores::test_hay_ganador_true PASSED          [ 53%]
tests/test_game.py::TestGanadores::test_hay_ganador_false PASSED         [ 53%]
tests/test_game.py::TestGanadores::test_ganador_con_fichas_en_barra PASSED [ 54%]
tests/test_game.py::TestGanadores::test_ganador_sin_fichas_en_barra PASSED [ 54%]
tests/test_game.py::TestCasosEdge::test_movimiento_con_todos_los_dados_iguales PASSED [ 54%]
tests/test_game.py::TestCasosEdge::test_reingreso_punto_destino_invalido PASSED [ 55%]
tests/test_game.py::TestCasosEdge::test_aplicar_movimiento_origen_y_destino_iguales PASSED [ 55%]
tests/test_game.py::TestCasosEdge::test_movimiento_jugador_o_direccion_correcta PASSED [ 55%]
tests/test_game.py::TestCasosEdge::test_movimiento_jugador_o_direccion_incorrecta PASSED [ 56%]
tests/test_game.py::TestCasosEdge::test_multiple_captura_en_partida PASSED [ 56%]
tests/test_game.py::TestCasosEdge::test_todos_los_puntos_posiciones_validas PASSED [ 56%]
tests/test_game.py::TestCasosEdge::test_reiniciar_mantiene_objetos PASSED [ 57%]
tests/test_game.py::TestBarraAdicionales::test_aplicar_movimiento_barra_sin_poder_reingresar PASSED [ 57%]
tests/test_game.py::TestBarraAdicionales::test_reingreso_jugador_o_con_captura PASSED [ 57%]
tests/test_game.py::TestBarraAdicionales::test_obtener_movimientos_barra_con_puntos_bloqueados PASSED [ 58%]
tests/test_player.py::test_str_jugador PASSED                            [ 58%]
tests/test_player.py::test_perder_ficha_multiples PASSED                 [ 58%]
tests/test_player.py::test_str_completo PASSED                           [ 59%]
tests/test_player.py::test_fichas_restantes PASSED                       [ 59%]
tests/test_player.py::test_perder_ficha PASSED                           [ 59%]
tests/test_player.py::test_perder_ficha_hasta_cero PASSED                [ 60%]
tests/test_player.py::test_jugador_con_nombre_largo PASSED               [ 60%]
tests/test_player.py::test_jugador_color_o PASSED                        [ 60%]
tests/test_player.py::test_jugador_color_x PASSED                        [ 61%]
tests/test_player.py::test_fichas_iniciales PASSED                       [ 61%]
tests/test_player.py::test_perder_ficha_consecutivas PASSED              [ 61%]
tests/test_player.py::test_nombre_vacio PASSED                           [ 62%]
tests/test_player.py::test_reiniciar_fichas PASSED                       [ 62%]
tests/test_player.py::test_igualdad_jugadores PASSED                     [ 63%]
tests/test_player.py::test_atributos_publicos PASSED                     [ 63%]
tests/test_player.py::test_metodos_disponibles PASSED                    [ 63%]
tests/test_player.py::test_estado_consistente PASSED                     [ 64%]
tests/test_player.py::test_edge_cases PASSED                             [ 64%]
tests/test_player.py::test_representaciones PASSED                       [ 64%]
tests/test_pygame_ui.py::TestBackgammonUI::test_ui_inicializacion PASSED [ 65%]
tests/test_pygame_ui.py::TestBackgammonUI::test_ui_tiene_screen PASSED   [ 65%]
tests/test_pygame_ui.py::TestBackgammonUI::test_punto_a_coordenadas_superior PASSED [ 65%]
tests/test_pygame_ui.py::TestBackgammonUI::test_punto_a_coordenadas_inferior PASSED [ 66%]
tests/test_pygame_ui.py::TestBackgammonUI::test_punto_a_coordenadas_con_fichas_apiladas PASSED [ 66%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_fuera_tablero_izquierda PASSED [ 66%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_fuera_tablero_arriba PASSED [ 67%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_valores_razonables PASSED [ 67%]
tests/test_pygame_ui.py::TestBackgammonUI::test_obtener_movimientos_validos_sin_dados PASSED [ 67%]
tests/test_pygame_ui.py::TestBackgammonUI::test_obtener_movimientos_validos_con_dados PASSED [ 68%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_quit PASSED [ 68%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_escape PASSED [ 68%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_espacio_primera_vez PASSED [ 69%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_espacio_con_dados_disponibles PASSED [ 69%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_espacio_juego_terminado PASSED [ 69%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_reinicio PASSED [ 70%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_pasar_turno_sin_dados PASSED [ 70%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_pasar_turno_con_movimientos PASSED [ 70%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_mouse_juego_terminado PASSED [ 71%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_mouse_sin_dados_tirados PASSED [ 71%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_mouse_fuera_tablero PASSED [ 71%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_con_coordenadas_centro PASSED [ 72%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_mouse_mover_ficha PASSED [ 72%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_varios_puntos PASSED [ 72%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_tablero PASSED   [ 73%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas PASSED    [ 73%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_con_seleccion PASSED [ 73%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_movimientos_validos PASSED [ 74%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_movimientos_validos_vacio PASSED [ 74%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_info_panel PASSED [ 75%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_info_panel_con_dados PASSED [ 75%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_info_panel_sin_dados PASSED [ 75%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_info_panel_mensaje_largo PASSED [ 76%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_info_panel_mensaje_corto PASSED [ 76%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_estado_normal PASSED [ 76%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_estado_juego_terminado PASSED [ 77%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_estado_ganador_2 PASSED [ 77%]
tests/test_pygame_ui.py::TestBackgammonUI::test_run_bucle_sale_inmediatamente PASSED [ 77%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_mouse_click PASSED [ 78%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_eventos_sin_eventos PASSED [ 78%]
tests/test_pygame_ui.py::TestBackgammonUI::test_todos_los_puntos_coordenadas PASSED [ 78%]
tests/test_pygame_ui.py::TestBackgammonUI::test_todos_los_puntos_multiples_fichas PASSED [ 79%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_bordes PASSED [ 79%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_barra_vacia PASSED [ 79%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_barra_con_fichas_x PASSED [ 80%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_barra_con_fichas_o PASSED [ 80%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_barra_ambas PASSED [ 80%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_fuera_sin_fichas PASSED [ 81%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_fuera_con_fichas PASSED [ 81%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_fichas_fuera_muchas_fichas PASSED [ 81%]
tests/test_pygame_ui.py::TestBackgammonUI::test_click_en_barra PASSED    [ 82%]
tests/test_pygame_ui.py::TestBackgammonUI::test_tiene_fichas_en_barra_ui PASSED [ 82%]
tests/test_pygame_ui.py::TestBackgammonUI::test_obtener_movimientos_validos_desde_barra_ui PASSED [ 82%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_metodo PASSED [ 83%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_con_barra_seleccionada PASSED [ 83%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_con_barra_seleccionada PASSED [ 83%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_puntos_superiores_columna_mayor_6 PASSED [ 84%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_puntos_inferiores_columna_mayor_6 PASSED [ 84%]
tests/test_pygame_ui.py::TestBackgammonUI::test_click_en_barra_jugador_x PASSED [ 84%]
tests/test_pygame_ui.py::TestBackgammonUI::test_click_en_barra_jugador_o PASSED [ 85%]
tests/test_pygame_ui.py::TestBackgammonUI::test_click_en_barra_sin_fichas PASSED [ 85%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_jugador_o PASSED [ 85%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_sin_dado_correcto PASSED [ 86%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_con_captura_x PASSED [ 86%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_con_captura_o PASSED [ 86%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_sin_fichas_en_barra_x PASSED [ 87%]
tests/test_pygame_ui.py::TestBackgammonUI::test_reingresar_desde_barra_sin_fichas_en_barra_o PASSED [ 87%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_seleccionar_barra_sin_fichas_disponibles PASSED [ 88%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_con_ficha_barra_seleccionada_movimiento_exitoso PASSED [ 88%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_con_ficha_barra_seleccionada_con_ganador PASSED [ 88%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_seleccionar_ficha_normal_sin_movimientos PASSED [ 89%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_seleccionar_ficha_enemiga PASSED [ 89%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_mover_ficha_con_ganador PASSED [ 89%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_mover_ficha_cambio_turno PASSED [ 90%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_movimiento_invalido PASSED [ 90%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_con_excepcion PASSED [ 90%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_con_barra_excepcion PASSED [ 91%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_columna_negativa PASSED [ 91%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_columna_mayor_11 PASSED [ 91%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_mitad_superior PASSED [ 92%]
tests/test_pygame_ui.py::TestBackgammonUI::test_coordenadas_a_punto_mitad_inferior PASSED [ 92%]
tests/test_pygame_ui.py::TestBackgammonUI::test_espacio_con_fichas_en_barra PASSED [ 92%]
tests/test_pygame_ui.py::TestBackgammonUI::test_pasar_turno_sin_dados_disponibles PASSED [ 93%]
tests/test_pygame_ui.py::TestBackgammonUI::test_pasar_turno_con_movimientos_desde_barra PASSED [ 93%]
tests/test_pygame_ui.py::TestBackgammonUI::test_pasar_turno_sin_movimientos_posibles PASSED [ 93%]
tests/test_pygame_ui.py::TestBackgammonUI::test_run_bucle_completo PASSED [ 94%]
tests/test_pygame_ui.py::TestBackgammonUI::test_dibujar_info_panel_con_fichas_en_barra PASSED [ 94%]
tests/test_pygame_ui.py::TestBackgammonUI::test_punto_a_coordenadas_superior_columna_menor_6 PASSED [ 94%]
tests/test_pygame_ui.py::TestBackgammonUI::test_punto_a_coordenadas_inferior_columna_menor_6 PASSED [ 95%]
tests/test_pygame_ui.py::TestBackgammonUI::test_punto_a_coordenadas_inferior_columna_mayor_6 PASSED [ 95%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_barra_jugador_incorrecto PASSED [ 95%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_barra_sin_movimientos_validos PASSED [ 96%]
tests/test_pygame_ui.py::TestBackgammonUI::test_manejar_click_punto_sin_dados_disponibles PASSED [ 96%]
tests/test_pygame_ui.py::TestBackgammonUI::test_obtener_movimientos_validos_con_varios_destinos PASSED [ 96%]
tests/test_pygame_ui.py::TestBackgammonUI::test_tiene_fichas_en_barra_jugador_o PASSED [ 97%]
tests/test_pygame_ui.py::test_ejecutar_pygame_ui PASSED                  [ 97%]
tests/test_pygame_ui.py::test_constantes_colores PASSED                  [ 97%]
tests/test_pygame_ui.py::test_constantes_colores_valores PASSED          [ 98%]
tests/test_pygame_ui.py::test_constantes_adicionales PASSED              [ 98%]
tests/test_pygame_ui.py::test_constantes_marrones PASSED                 [ 98%]
tests/test_resource.py::test_constantes_colores PASSED                   [ 99%]
tests/test_resource.py::test_constantes_ventana PASSED                   [ 99%]
tests/test_resource.py::test_clase_recurso_descripcion PASSED            [100%]

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
cli/__init__.py        0      0   100%
cli/cli.py           318     30    91%   72, 84, 151, 166-167, 224, 298-299, 334-337, 362-370, 408, 410-411, 413-414, 418, 425, 452-453, 457
core/__init__.py       2      0   100%
core/board.py         94      3    97%   137, 139, 162
core/dice.py          12      0   100%
core/game.py         178      3    98%   168-169, 250
core/player.py        12      0   100%
ui/__init__.py         0      0   100%
ui/pygame_ui.py      454      7    98%   199, 313, 506, 530-531, 580, 744
------------------------------------------------
TOTAL               1070     43    96%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml

Required test coverage of 90% reached. Total coverage: 95.98%

============================= 292 passed in 0.76s ==============================

```

---

## 📈 Cobertura de Código

```
tests/test_pygame_ui.py::test_ejecutar_pygame_ui PASSED                  [ 97%]
tests/test_pygame_ui.py::test_constantes_colores PASSED                  [ 97%]
tests/test_pygame_ui.py::test_constantes_colores_valores PASSED          [ 98%]
tests/test_pygame_ui.py::test_constantes_adicionales PASSED              [ 98%]
tests/test_pygame_ui.py::test_constantes_marrones PASSED                 [ 98%]
tests/test_resource.py::test_constantes_colores PASSED                   [ 99%]
tests/test_resource.py::test_constantes_ventana PASSED                   [ 99%]
tests/test_resource.py::test_clase_recurso_descripcion PASSED            [100%]

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
cli/__init__.py        0      0   100%
cli/cli.py           318     35    89%   72, 84, 151, 166-167, 224, 298-299, 325-337, 362-370, 408, 410-411, 413-414, 418, 425, 452-453, 457
core/__init__.py       2      0   100%
core/board.py         94      3    97%   137, 139, 162
core/dice.py          12      0   100%
core/game.py         178      3    98%   168-169, 250
core/player.py        12      0   100%
ui/__init__.py         0      0   100%
ui/pygame_ui.py      454      7    98%   199, 313, 506, 530-531, 580, 744
------------------------------------------------
TOTAL               1070     48    96%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml

Required test coverage of 90% reached. Total coverage: 95.51%

============================= 292 passed in 0.79s ==============================

```

---

## 📄 Archivos Generados

- `htmlcov/index.html` - Reporte HTML
- `coverage.xml` - XML para Codecov

---

**Generado localmente** 💻
