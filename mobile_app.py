import flet as ft

def main(page: ft.Page):
    page.title = "FocusGrid Mobile"
    page.background_color = "#0A0D14"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # Mobile Header Block
    header = ft.Column([
        ft.Text("🎮 FocusGrid", size=28, weight=ft.FontWeight.BOLD, color="white"),
        ft.Text("Mobile Accountability Node", size=14, color="#64748B")
    ], spacing=4, alignment=ft.MainAxisAlignment.CENTER)
    
    # 3D Emulated Focus Card
    focus_card = ft.Container(
        content=ft.Column([
            ft.Text("Active Session", size=18, weight=ft.FontWeight.W_600, color="white"),
            ft.Text("Status: In Flow State", size=14, color="#A855F7"),
            ft.Divider(color="#202A3F"),
            ft.ElevatedButton(
                content=ft.Text("🚪 Check-Out of Grid", color="white"),  # <--- Wrapped inside ft.Text assigned to content
                bgcolor="#8B5CF6",
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                width=250
        
            )
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=25,
        border_radius=20,
        bgcolor="#121824",
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color="#040609", offset=ft.Offset(5, 5))
    )
    
    # Mobile Co-worker Stream Rows
    peer_header = ft.Text("👥 Room Activity", size=16, weight=ft.FontWeight.W_500, color="white")
    
    def build_peer_tile(name, time_str):
        return ft.Container(
            content=ft.Row([
                ft.Icon(name="person", color="#8B5CF6"), # 💡 Safe string name
                ft.Column([
                    ft.Text(name, size=14, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Text(time_str, size=11, color="#64748B")
                ], spacing=2)
            ]),
            padding=12,
            border_radius=12,
            bgcolor="#1A2333"
    )

    peer_list = ft.Column([
        build_peer_tile("Rahul K.", "Focus State: 45m"),
        build_peer_tile("Priya M.", "Focus State: 22m")
    ], spacing=10)

    # Assemble Phone Interface View Layout
    page.add(
        header,
        ft.Container(height=15),
        focus_card,
        ft.Container(height=20),
        peer_header,
        ft.Container(height=5),
        peer_list
    )

if __name__ == "__main__":
    ft.app(target=main)