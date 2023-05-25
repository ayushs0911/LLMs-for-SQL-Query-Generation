import openai
import os
import logging

import openai

def insert_table_schema():
    table_input = input("Enter name of the table : ")
    col = [input("Column names : ")]
    columns = " ".join(col).split()
    return table_input, columns


# def create_table_definition_prompt(df, table_name):
#     prompt = '''### MySql table, with its properties:
# #
# # Table Name: {} and Columns : {}
# #
# '''.format(table_name, df)
#     return prompt


def create_table_definition_prompt(df, table_name):
    prompt = "### MySql table, with its properties\n\n"
    prompt += f"Table Name: {table_name}\n\n"
    prompt += "Column Names:\n"

    for column_name in df:
        prompt += f"- {column_name}\n"

    return prompt


def user_query_input():
    user_input = input("Tell what you want to know about the data: \n")
    return user_input


def combine_prompts(fixed_sql_prompt, user_query):
    final_user_input = f"### A query to answer: {user_query}\nSELECT"
    return fixed_sql_prompt + final_user_input


def send_to_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1,
    )
    return response


openai.api_key = "Enter Your Secret Key"

if __name__ == "__main__":
    table, column_name = insert_table_schema()
    z = create_table_definition_prompt(df=column_name, table_name=table)
    input = user_query_input()
    combined = combine_prompts(fixed_sql_prompt = z, user_query=input)
    # print(combined)
    response = send_to_openai(prompt = combined)
    proposed_query = "Select" + response["choices"][0]["text"]
    print(proposed_query)
