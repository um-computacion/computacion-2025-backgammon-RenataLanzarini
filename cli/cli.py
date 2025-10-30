"""
Interfaz de línea de comandos SIMPLIFICADA para Backgammon.
Versión con ayuda interactiva y sugerencias automáticas.
"""

from core.game import BackgammonJuego


class BackgammonCLI:
    """CLI simplificada con guía paso a paso."""
    
    def __init__(self):
        """Inicializa la CLI."""
        self.__juego__ = BackgammonJuego()
        self.modo_tutorial = True  # Modo tutorial activado por defecto

    def mostrar_tablero_visual(self):
        """Muestra el tablero de forma visual."""
        tablero = self.__juego__.tablero
        
        print("\n" + "=" * 80)
        print("                        🎲 BACKGAMMON - TABLERO 🎲")
        print("=" * 80)
        
        # Encabezado superior
        print("\n  13  14  15  16  17  18 |BAR| 19  20  21  22  23  24")
        print(" " + "-" * 77)
        
        # Parte superior
        for fila in range(5):
            linea = " "
            for punto in range(12, 18):
                simbolo = self._obtener_simbolo(tablero, punto, fila)
                linea += f" {simbolo}  "
            linea += self._formato_barra(fila)
            for punto in range(18, 24):
                simbolo = self._obtener_simbolo(tablero, punto, fila)
                linea += f" {simbolo}  "
            print(linea)
        
        print(" " + "-" * 77)
        
        # Parte inferior
        for fila in range(4, -1, -1):
            linea = " "
            for punto in range(11, 5, -1):
                simbolo = self._obtener_simbolo(tablero, punto, fila)
                linea += f" {simbolo}  "
            linea += "|  | "
            for punto in range(5, -1, -1):
                simbolo = self._obtener_simbolo(tablero, punto, fila)
                linea += f" {simbolo}  "
            print(linea)
        
        print(" " + "-" * 77)
        print("  12  11  10   9   8   7 |BAR|  6   5   4   3   2   1")
        
        self._mostrar_info_barra()
        self._mostrar_dados_con_ayuda()
        
        print("=" * 80 + "\n")

    def _obtener_simbolo(self, tablero, punto, fila):
        """Obtiene el símbolo para una posición."""
        cantidad = tablero.fichas_en(punto)
        if cantidad == 0:
            return " "
        if fila < min(cantidad, 5):
            return tablero.ficha_en(punto) or " "
        elif fila == 4 and cantidad > 5:
            return str(cantidad)
        return " "

    def _formato_barra(self, fila):
        """Formatea la barra."""
        barra_x = len(self.__juego__.tablero.barra_x)
        barra_o = len(self.__juego__.tablero.barra_o)
        
        linea = "|"
        if fila == 0 and barra_x > 0:
            linea += f"X{barra_x:1d}"
        elif fila == 1 and barra_o > 0:
            linea += f"O{barra_o:1d}"
        else:
            linea += "  "
        linea += "| "
        return linea

    def _mostrar_info_barra(self):
        """Muestra info de la barra."""
        barra_x = len(self.__juego__.tablero.barra_x)
        barra_o = len(self.__juego__.tablero.barra_o)
        
        if barra_x > 0 or barra_o > 0:
            print(f"\n 📊 Fichas en barra: X={barra_x}, O={barra_o}")

    def _mostrar_dados_con_ayuda(self):
        """Muestra dados con ayuda contextual."""
        ficha = 'X' if self.__juego__.turno == 1 else 'O'
        print(f"\n 👤 Turno: Jugador {ficha}")
        
        if self.__juego__.dados_disponibles:
            print(f" 🎲 Dados disponibles: {self.__juego__.dados_disponibles}")
            
            if self.modo_tutorial:
                self._mostrar_sugerencias()
        else:
            print(" ⏸️  Escribe 'tirar' para lanzar los dados")

    def _mostrar_sugerencias(self):
        """Muestra sugerencias de movimientos posibles."""
        print("\n 💡 SUGERENCIAS DE MOVIMIENTO:")
        
        ficha_jugador = "X" if self.__juego__.turno == 1 else "O"
        
        # Ver si hay fichas en barra
        if self.__juego__.tablero.tiene_fichas_en_barra(ficha_jugador):
            print("    ⚠️  ¡Tienes fichas en la barra! Debes reingresarlas primero.")
            print("    Ejemplo: mover -1 3  (reingresa al punto 3)")
            return
        
        # Buscar puntos con fichas del jugador
        sugerencias = []
        for punto in range(24):
            if not self.__juego__.tablero.esta_vacio(punto):
                if self.__juego__.tablero.ficha_en(punto) == ficha_jugador:
                    # Probar cada dado disponible
                    for dado in self.__juego__.dados_disponibles:
                        if self.__juego__.turno == 1:
                            destino = punto + dado
                        else:
                            destino = punto - dado
                        
                        if 0 <= destino < 24:
                            if self.__juego__.es_movimiento_valido(punto, destino):
                                sugerencias.append((punto + 1, destino + 1, dado))
                                if len(sugerencias) >= 3:
                                    break
            if len(sugerencias) >= 3:
                break
        
        if sugerencias:
            print("    Movimientos posibles:")
            for origen, destino, dado in sugerencias:
                print(f"    → mover {origen} {destino}  (usa dado {dado})")
        else:
            print("    ⚠️  No hay movimientos posibles con estos dados")
            print("    El turno pasará automáticamente")

    def mostrar_ayuda(self):
        """Muestra ayuda simplificada."""
        print("\n" + "=" * 70)
        print("                    📋 AYUDA RÁPIDA")
        print("=" * 70)
        print("\n  🎮 CÓMO JUGAR:")
        print("    1. Escribe 'tirar' para lanzar los dados")
        print("    2. Mira las SUGERENCIAS que aparecen")
        print("    3. Copia un comando sugerido, por ejemplo:")
        print("       → mover 12 8")
        print("    4. Repite hasta usar todos los dados")
        print("\n  📝 COMANDOS:")
        print("    tirar       - Lanza los dados")
        print("    mover X Y   - Mueve del punto X al Y")
        print("    tablero     - Muestra el tablero")
        print("    ayuda       - Esta ayuda")
        print("    tutorial    - Activa/desactiva sugerencias")
        print("    salir       - Sale del juego")
        print("\n  💡 RECUERDA:")
        print("    • Jugador X mueve hacia ADELANTE (1 → 24)")
        print("    • Jugador O mueve hacia ATRÁS (24 → 1)")
        print("    • Copia las sugerencias para jugar fácil")
        print("=" * 70 + "\n")

    def mostrar_bienvenida(self):
        """Muestra bienvenida."""
        print("\n" + "=" * 80)
        print("""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║               🎲  B A C K G A M M O N  -  C L I  🎲                  ║
    ║                       VERSIÓN SIMPLIFICADA                           ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝
        """)
        print("=" * 80)
        print("\n  🎓 MODO TUTORIAL ACTIVADO")
        print("     El juego te sugerirá movimientos posibles")
        print("     Solo copia y pega los comandos sugeridos")
        print("\n" + "=" * 80 + "\n")

    def iniciar(self):
        """Inicia el juego."""
        self.mostrar_bienvenida()
        self.__juego__.iniciar()
        print("✅ Juego iniciado. Escribe 'ayuda' si tienes dudas.\n")
        self.mostrar_tablero_visual()

        while True:
            ganador = self.__juego__.verificar_ganador()
            if ganador:
                self._mostrar_victoria(ganador)
            
            cmd = input("> ").strip().lower()
            
            if not cmd:
                continue
            
            if cmd in ("salir", "exit", "q"):
                self.salir()
                break
            
            if cmd in ("ayuda", "help", "h", "?"):
                self.mostrar_ayuda()
                continue
            
            if cmd == "tablero":
                self.mostrar_tablero_visual()
                continue
            
            if cmd == "tutorial":
                self.modo_tutorial = not self.modo_tutorial
                estado = "activado" if self.modo_tutorial else "desactivado"
                print(f"\n✅ Modo tutorial {estado}\n")
                continue
            
            if cmd == "estado":
                self.mostrar_estado()
                continue
            
            if cmd == "reiniciar":
                self.reiniciar_juego()
                continue
            
            if cmd == "tirar":
                self._procesar_tirada(ganador)
                continue
            
            if cmd.startswith("mover"):
                self._procesar_movimiento(cmd, ganador)
                continue
            
            print("❌ Comando no reconocido. Escribe 'ayuda' para ver los comandos.")

    def _mostrar_victoria(self, ganador):
        """Muestra mensaje de victoria."""
        print("\n" + "🎉" * 40)
        print(f"\n          ¡¡¡ JUGADOR {ganador} HA GANADO !!!")
        print("\n" + "🎉" * 40)
        print("\n  Escribe 'reiniciar' para jugar de nuevo\n")

    def _procesar_tirada(self, ganador):
        """Procesa tirada de dados."""
        if ganador:
            print("⚠️  La partida terminó. Escribe 'reiniciar'\n")
            return
        
        if self.__juego__.dados_disponibles:
            print("⚠️  Ya tienes dados. Úsalos primero.")
            print(f"   Dados: {self.__juego__.dados_disponibles}\n")
            return
        
        vals = self.__juego__.tirar_dados()
        print(f"\n🎲 Dados tirados: {vals}")
        
        # Mostrar tablero automáticamente con sugerencias
        self.mostrar_tablero_visual()

    def _procesar_movimiento(self, cmd, ganador):
        """Procesa movimiento."""
        if ganador:
            print("⚠️  La partida terminó. Escribe 'reiniciar'\n")
            return
        
        parts = cmd.split()
        if len(parts) != 3:
            print("❌ Formato: mover X Y")
            print("   Ejemplo: mover 12 8\n")
            return
        
        try:
            origen_input = int(parts[1])
            destino_input = int(parts[2])
            
            # Convertir a índices
            origen = origen_input if origen_input == -1 else origen_input - 1
            destino = destino_input - 1
            
        except ValueError:
            print("❌ Los números deben ser enteros\n")
            return
        
        # Explicar por qué falló ANTES de aplicar
        if not self.__juego__.es_movimiento_valido(origen, destino):
            self._explicar_error_movimiento(origen, destino, origen_input, destino_input)
            return
        
        # Aplicar movimiento
        ok = self.__juego__.aplicar_movimiento(origen, destino)
        if ok:
            print(f"✅ Movido: {origen_input} → {destino_input}")
            
            # Mostrar tablero actualizado
            self.mostrar_tablero_visual()
            
            # Verificar si terminó el turno
            if not self.__juego__.tiene_dados_disponibles():
                self.__juego__.cambiar_turno()
                ficha = 'X' if self.__juego__.turno == 1 else 'O'
                print(f"🔄 Turno del Jugador {ficha}")
                print("   Escribe 'tirar' para lanzar dados\n")

    def _explicar_error_movimiento(self, origen, destino, origen_input, destino_input):
        """Explica por qué falló un movimiento."""
        print(f"\n❌ No puedes mover {origen_input} → {destino_input}")
        
        ficha_jugador = "X" if self.__juego__.turno == 1 else "O"
        
        # Verificar cada condición
        if origen != -1 and self.__juego__.tablero.esta_vacio(origen):
            print(f"   Razón: El punto {origen_input} está vacío")
        elif origen != -1 and self.__juego__.tablero.ficha_en(origen) != ficha_jugador:
            ficha_en_origen = self.__juego__.tablero.ficha_en(origen)
            print(f"   Razón: El punto {origen_input} tiene fichas {ficha_en_origen}, no tuyas ({ficha_jugador})")
        elif self.__juego__.tablero.tiene_fichas_en_barra(ficha_jugador) and origen != -1:
            print(f"   Razón: Tienes fichas en la barra, debes reingresarlas primero")
            print(f"   Usa: mover -1 Y")
        else:
            # Calcular distancia
            if origen == -1:
                distancia = destino + 1
            else:
                distancia = abs(destino - origen)
            
            if distancia not in self.__juego__.dados_disponibles:
                print(f"   Razón: La distancia es {distancia}, pero tus dados son {self.__juego__.dados_disponibles}")
            else:
                print(f"   Razón: El punto {destino_input} está bloqueado por el oponente")
        
        print("\n   💡 Mira las SUGERENCIAS arriba para ver movimientos válidos\n")

    def mostrar_estado(self):
        """Muestra estado."""
        print("\n" + "─" * 70)
        print("📊 ESTADO")
        print("─" * 70)
        print(self.__juego__.descripcion())
        print("─" * 70 + "\n")

    def reiniciar_juego(self):
        """Reinicia el juego."""
        self.__juego__.reiniciar()
        print("\n🔄 Juego reiniciado\n")
        self.mostrar_tablero_visual()

    def salir(self):
        """Sale del juego."""
        print("\n" + "=" * 70)
        print("\n          👋 ¡Gracias por jugar!")
        print("\n" + "=" * 70 + "\n")


def ejecutar_cli():
    """Ejecuta la CLI."""
    cli = BackgammonCLI()
    cli.iniciar()
