from token_definition import *
from scanner_simulator import *

class AFD(object):
    def __init__(self):
        self.regex = ['(', '(', 32, '|', 9, '|', 10, ')', '+', ')', '#ws', '|', '(', '(', 65, '|', 66, '|', 67, '|', 68, '|', 69, '|', 70, '|', 71, '|', 72, '|', 73, '|', 74, '|', 75, '|', 76, '|', 77, '|', 78, '|', 79, '|', 80, '|', 81, '|', 82, '|', 83, '|', 84, '|', 85, '|', 86, '|', 87, '|', 88, '|', 89, '|', 90, '|', 97, '|', 98, '|', 99, '|', 100, '|', 101, '|', 102, '|', 103, '|', 104, '|', 105, '|', 106, '|', 107, '|', 108, '|', 109, '|', 110, '|', 111, '|', 112, '|', 113, '|', 114, '|', 115, '|', 116, '|', 117, '|', 118, '|', 119, '|', 120, '|', 121, '|', 122, ')', '(', '(', 65, '|', 66, '|', 67, '|', 68, '|', 69, '|', 70, '|', 71, '|', 72, '|', 73, '|', 74, '|', 75, '|', 76, '|', 77, '|', 78, '|', 79, '|', 80, '|', 81, '|', 82, '|', 83, '|', 84, '|', 85, '|', 86, '|', 87, '|', 88, '|', 89, '|', 90, '|', 97, '|', 98, '|', 99, '|', 100, '|', 101, '|', 102, '|', 103, '|', 104, '|', 105, '|', 106, '|', 107, '|', 108, '|', 109, '|', 110, '|', 111, '|', 112, '|', 113, '|', 114, '|', 115, '|', 116, '|', 117, '|', 118, '|', 119, '|', 120, '|', 121, '|', 122, ')', '|', '(', '(', '_', ')', '*', ')', '|', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', ')', '*', ')', '#id', '|', '(', '(', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', '+', ')', '(', 46, '(', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', '+', ')', ')', '?', '(', 69, '(', 43, '|', 45, ')', '?', '(', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', '+', ')', ')', '?', ')', '#number', '|', 59, '#;', '|', 58, 61, '#:=', '|', 60, '#<', '|', 61, '#=', '|', 43, '#+', '|', 45, '#-', '|', 42, '#*', '|', 47, '#/', '|', 40, '#(', '|', 41, '#)']
        self.states = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19']
        self.transitions = [['S0', 32, 'S1'], ['S0', 9, 'S1'], ['S0', 10, 'S1'], ['S0', 65, 'S2'], ['S0', 66, 'S2'], ['S0', 67, 'S2'], ['S0', 68, 'S2'], ['S0', 69, 'S2'], ['S0', 70, 'S2'], ['S0', 71, 'S2'], ['S0', 72, 'S2'], ['S0', 73, 'S2'], ['S0', 74, 'S2'], ['S0', 75, 'S2'], ['S0', 76, 'S2'], ['S0', 77, 'S2'], ['S0', 78, 'S2'], ['S0', 79, 'S2'], ['S0', 80, 'S2'], ['S0', 81, 'S2'], ['S0', 82, 'S2'], ['S0', 83, 'S2'], ['S0', 84, 'S2'], ['S0', 85, 'S2'], ['S0', 86, 'S2'], ['S0', 87, 'S2'], ['S0', 88, 'S2'], ['S0', 89, 'S2'], ['S0', 90, 'S2'], ['S0', 97, 'S2'], ['S0', 98, 'S2'], ['S0', 99, 'S2'], ['S0', 100, 'S2'], ['S0', 101, 'S2'], ['S0', 102, 'S2'], ['S0', 103, 'S2'], ['S0', 104, 'S2'], ['S0', 105, 'S2'], ['S0', 106, 'S2'], ['S0', 107, 'S2'], ['S0', 108, 'S2'], ['S0', 109, 'S2'], ['S0', 110, 'S2'], ['S0', 111, 'S2'], ['S0', 112, 'S2'], ['S0', 113, 'S2'], ['S0', 114, 'S2'], ['S0', 115, 'S2'], ['S0', 116, 'S2'], ['S0', 117, 'S2'], ['S0', 118, 'S2'], ['S0', 119, 'S2'], ['S0', 120, 'S2'], ['S0', 121, 'S2'], ['S0', 122, 'S2'], ['S0', 48, 'S3'], ['S0', 49, 'S3'], ['S0', 50, 'S3'], ['S0', 51, 'S3'], ['S0', 52, 'S3'], ['S0', 53, 'S3'], ['S0', 54, 'S3'], ['S0', 55, 'S3'], ['S0', 56, 'S3'], ['S0', 57, 'S3'], ['S0', 43, 'S4'], ['S0', 45, 'S5'], ['S0', 59, 'S6'], ['S0', 58, 'S7'], ['S0', 61, 'S8'], ['S0', 60, 'S9'], ['S0', 42, 'S10'], ['S0', 47, 'S11'], ['S0', 40, 'S12'], ['S0', 41, 'S13'], ['S1', 32, 'S1'], ['S1', 9, 'S1'], ['S1', 10, 'S1'], ['S2', 65, 'S2'], ['S2', 66, 'S2'], ['S2', 67, 'S2'], ['S2', 68, 'S2'], ['S2', 69, 'S2'], ['S2', 70, 'S2'], ['S2', 71, 'S2'], ['S2', 72, 'S2'], ['S2', 73, 'S2'], ['S2', 74, 'S2'], ['S2', 75, 'S2'], ['S2', 76, 'S2'], ['S2', 77, 'S2'], ['S2', 78, 'S2'], ['S2', 79, 'S2'], ['S2', 80, 'S2'], ['S2', 81, 'S2'], ['S2', 82, 'S2'], ['S2', 83, 'S2'], ['S2', 84, 'S2'], ['S2', 85, 'S2'], ['S2', 86, 'S2'], ['S2', 87, 'S2'], ['S2', 88, 'S2'], ['S2', 89, 'S2'], ['S2', 90, 'S2'], ['S2', 97, 'S2'], ['S2', 98, 'S2'], ['S2', 99, 'S2'], ['S2', 100, 'S2'], ['S2', 101, 'S2'], ['S2', 102, 'S2'], ['S2', 103, 'S2'], ['S2', 104, 'S2'], ['S2', 105, 'S2'], ['S2', 106, 'S2'], ['S2', 107, 'S2'], ['S2', 108, 'S2'], ['S2', 109, 'S2'], ['S2', 110, 'S2'], ['S2', 111, 'S2'], ['S2', 112, 'S2'], ['S2', 113, 'S2'], ['S2', 114, 'S2'], ['S2', 115, 'S2'], ['S2', 116, 'S2'], ['S2', 117, 'S2'], ['S2', 118, 'S2'], ['S2', 119, 'S2'], ['S2', 120, 'S2'], ['S2', 121, 'S2'], ['S2', 122, 'S2'], ['S2', '_', 'S2'], ['S2', 48, 'S2'], ['S2', 49, 'S2'], ['S2', 50, 'S2'], ['S2', 51, 'S2'], ['S2', 52, 'S2'], ['S2', 53, 'S2'], ['S2', 54, 'S2'], ['S2', 55, 'S2'], ['S2', 56, 'S2'], ['S2', 57, 'S2'], ['S3', 69, 'S14'], ['S3', 48, 'S3'], ['S3', 49, 'S3'], ['S3', 50, 'S3'], ['S3', 51, 'S3'], ['S3', 52, 'S3'], ['S3', 53, 'S3'], ['S3', 54, 'S3'], ['S3', 55, 'S3'], ['S3', 56, 'S3'], ['S3', 57, 'S3'], ['S3', 46, 'S15'], ['S7', 61, 'S16'], ['S14', 48, 'S17'], ['S14', 49, 'S17'], ['S14', 50, 'S17'], ['S14', 51, 'S17'], ['S14', 52, 'S17'], ['S14', 53, 'S17'], ['S14', 54, 'S17'], ['S14', 55, 'S17'], ['S14', 56, 'S17'], ['S14', 57, 'S17'], ['S14', 43, 'S18'], ['S14', 45, 'S18'], ['S15', 48, 'S19'], ['S15', 49, 'S19'], ['S15', 50, 'S19'], ['S15', 51, 'S19'], ['S15', 52, 'S19'], ['S15', 53, 'S19'], ['S15', 54, 'S19'], ['S15', 55, 'S19'], ['S15', 56, 'S19'], ['S15', 57, 'S19'], ['S17', 48, 'S17'], ['S17', 49, 'S17'], ['S17', 50, 'S17'], ['S17', 51, 'S17'], ['S17', 52, 'S17'], ['S17', 53, 'S17'], ['S17', 54, 'S17'], ['S17', 55, 'S17'], ['S17', 56, 'S17'], ['S17', 57, 'S17'], ['S18', 48, 'S17'], ['S18', 49, 'S17'], ['S18', 50, 'S17'], ['S18', 51, 'S17'], ['S18', 52, 'S17'], ['S18', 53, 'S17'], ['S18', 54, 'S17'], ['S18', 55, 'S17'], ['S18', 56, 'S17'], ['S18', 57, 'S17'], ['S19', 69, 'S14'], ['S19', 48, 'S19'], ['S19', 49, 'S19'], ['S19', 50, 'S19'], ['S19', 51, 'S19'], ['S19', 52, 'S19'], ['S19', 53, 'S19'], ['S19', 54, 'S19'], ['S19', 55, 'S19'], ['S19', 56, 'S19'], ['S19', 57, 'S19']]
        self.initial_state = 'S0'
        self.final_states = {'S1': '#ws', 'S2': '#id', 'S3': '#number', 'S4': '#+', 'S5': '#-', 'S6': '#;', 'S8': '#=', 'S9': '#<', 'S10': '#*', 'S11': '#/', 'S12': '#(', 'S13': '#)', 'S16': '#:=', 'S17': '#number', 'S19': '#number'}
        self.symbols = [32, 9, 10, '#ws', 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, '_', 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, '#id', 46, 43, 45, '#number', 59, '#;', 58, 61, '#:=', 60, '#<', '#=', '#+', '#-', 42, '#*', 47, '#/', 40, '#(', 41, '#)']

def tokenScanner(token):
	if(token == '#ws'):
		return WHITESPACE
	if(token == '#id'):
		return ID
	if(token == '#number'):
		return NUMBER
	if(token == '#;'):
		return SEMICOLON
	if(token == '#:='):
		return ASSIGNOP
	if(token == '#<'):
		return LT
	if(token == '#='):
		return EQ
	if(token == '#+'):
		return PLUS
	if(token == '#-'):
		return MINUS
	if(token == '#*'):
		return TIMES
	if(token == '#/'):
		return DIV
	if(token == '#('):
		return LPAREN
	if(token == '#)'):
		return RPAREN

	return ERROR

afd = AFD()
simulation('./tests/token_test.txt', tokenScanner, afd)