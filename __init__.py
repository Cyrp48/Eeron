from flask import Flask, render_template, request, jsonify
from .database import init_db, get_tasks, add_task, delete_task, mark_task_done
import sqlite3