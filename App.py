import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 350, 570
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Marks Calculator")

# Colors
BG_COLOR = (36, 36, 36)
TEXT_COLOR = (240, 240, 240)
GRAY = (150, 150, 150)
INPUT_BG_ACTIVE = (50, 50, 50)
INPUT_BG_INACTIVE = (40, 40, 40)
BUTTON_COLOR = (31, 106, 165)
BUTTON_HOVER = (20, 72, 112)
WARN_COLOR = (231, 76, 60)

font_title = pygame.font.SysFont("segoeui", 32, bold=True)
font_label = pygame.font.SysFont("segoeui", 16)
font_input = pygame.font.SysFont("segoeui", 18)
font_info = pygame.font.SysFont("segoeui", 14, italic=True)
font_bold = pygame.font.SysFont("segoeui", 16, bold=True)

font_result_lbl = pygame.font.SysFont("segoeui", 20, bold=True)
font_result_val = pygame.font.SysFont("segoeui", 22, bold=True)
font_grade = pygame.font.SysFont("segoeui", 36, bold=True)

GRADE_COLORS = {
    "A": (46, 204, 113),  # #2ecc71
    "B": (52, 152, 219),  # #3498db
    "C": (241, 196, 15),  # #f1c40f
    "D": (230, 126, 34),  # #e67e22
    "F": (231, 76, 60)    # #e74c3c
}

# State
math_text = ""
science_text = ""
english_text = ""
active_input = None  # 0: math, 1: science, 2: english

error_message = ""
total_result = "0.0 / 300"
percentage_result = "0.00%"
grade_result = "-"
grade_color = TEXT_COLOR

def calculate():
    global error_message, total_result, percentage_result, grade_result, grade_color
    try:
        error_message = ""
        m = float(math_text)
        s = float(science_text)
        e = float(english_text)
        
        if any(x < 0 or x > 100 for x in [m, s, e]):
            error_message = "Marks must be between 0 and 100."
            return
            
        total = m + s + e
        perc = (total / 300.0) * 100.0
        
        if perc >= 90:
            grade = "A"
        elif perc >= 80:
            grade = "B"
        elif perc >= 70:
            grade = "C"
        elif perc >= 60:
            grade = "D"
        else:
            grade = "F"
            
        total_result = f"{total:.1f} / 300"
        percentage_result = f"{perc:.2f}%"
        grade_result = grade
        grade_color = GRADE_COLORS[grade]
        
    except ValueError:
        error_message = "Please enter valid numbers."

# Main loop
clock = pygame.time.Clock()

input_rects = [
    pygame.Rect(50, 140, 250, 35),
    pygame.Rect(50, 220, 250, 35),
    pygame.Rect(50, 300, 250, 35)
]
button_rect = pygame.Rect(75, 370, 200, 40)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                active_input = None
                for i, rect in enumerate(input_rects):
                    if rect.collidepoint(mouse_pos):
                        active_input = i
                
                if button_rect.collidepoint(mouse_pos):
                    calculate()
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                calculate()
            elif event.key == pygame.K_TAB:
                if active_input is not None:
                    active_input = (active_input + 1) % 3
                else:
                    active_input = 0
            elif active_input is not None:
                if event.key == pygame.K_BACKSPACE:
                    if active_input == 0:
                        math_text = math_text[:-1]
                    elif active_input == 1:
                        science_text = science_text[:-1]
                    elif active_input == 2:
                        english_text = english_text[:-1]
                else:
                    char = event.unicode
                    if char.isdigit() or char == '.':
                        if active_input == 0:
                            math_text += char
                        elif active_input == 1:
                            science_text += char
                        elif active_input == 2:
                            english_text += char
                            
    screen.fill(BG_COLOR)
    
    # Draw Title
    title_surface = font_title.render("Marks Calculator", True, TEXT_COLOR)
    screen.blit(title_surface, (WIDTH//2 - title_surface.get_width()//2, 20))
    
    info_surface = font_info.render("(Enter marks out of 100 for each subject)", True, GRAY)
    screen.blit(info_surface, (WIDTH//2 - info_surface.get_width()//2, 55))
    
    # Draw Inputs
    labels = ["Math Marks:", "Science Marks:", "English Marks:"]
    texts = [math_text, science_text, english_text]
    
    for i in range(3):
        label_surf = font_label.render(labels[i], True, TEXT_COLOR)
        screen.blit(label_surf, (input_rects[i].x, input_rects[i].y - 25))
        
        color = INPUT_BG_ACTIVE if active_input == i else INPUT_BG_INACTIVE
        pygame.draw.rect(screen, color, input_rects[i], border_radius=5)
        
        # Border
        border_color = BUTTON_COLOR if active_input == i else GRAY
        pygame.draw.rect(screen, border_color, input_rects[i], 2, border_radius=5)
        
        # Text
        txt_surf = font_input.render(texts[i], True, TEXT_COLOR)
        if not texts[i] and active_input != i:
            ph_surf = font_input.render("max 100", True, GRAY)
            screen.blit(ph_surf, (input_rects[i].x + input_rects[i].width//2 - ph_surf.get_width()//2, input_rects[i].y + 7))
        else:
            screen.blit(txt_surf, (input_rects[i].x + input_rects[i].width//2 - txt_surf.get_width()//2, input_rects[i].y + 7))
        
    # Draw Button
    btn_color = BUTTON_HOVER if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, btn_color, button_rect, border_radius=8)
    btn_txt = font_bold.render("Calculate Results", True, TEXT_COLOR)
    screen.blit(btn_txt, (button_rect.x + button_rect.width//2 - btn_txt.get_width()//2, button_rect.y + 10))
    
    # Draw Error Message
    if error_message:
        err_surf = font_label.render(error_message, True, WARN_COLOR)
        screen.blit(err_surf, (WIDTH//2 - err_surf.get_width()//2, 420))
        
    # Draw Results
    res_y = 440
    
    # Total
    tot_lbl = font_result_lbl.render("Total:", True, TEXT_COLOR)
    tot_val = font_result_val.render(total_result, True, TEXT_COLOR)
    screen.blit(tot_lbl, (50, res_y))
    screen.blit(tot_val, (190, res_y - 2))
    
    # Percentage
    perc_lbl = font_result_lbl.render("Percentage:", True, TEXT_COLOR)
    perc_val = font_result_val.render(percentage_result, True, TEXT_COLOR)
    screen.blit(perc_lbl, (50, res_y + 40))
    screen.blit(perc_val, (190, res_y + 38))
    
    # Grade
    grd_lbl = font_result_lbl.render("Grade:", True, TEXT_COLOR)
    grd_val = font_grade.render(grade_result, True, grade_color)
    screen.blit(grd_lbl, (50, res_y + 80))
    screen.blit(grd_val, (190, res_y + 70))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()