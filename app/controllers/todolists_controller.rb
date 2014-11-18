class TodolistsController < ApplicationController
  before_action :set_todolist, only: [:show, :edit, :update, :destroy]

  def index
    @todolists = Todolist.all
  end

  def show
  end

  def new
    @todolist = Todolist.new
  end

  def edit
  end

  def create
    @todolist = Todolist.new(todolist_params)
    @todolist.save
    redirect_to todolists_path
  end

  def update
    @todolist.update(todolist_params)
    redirect_to todolists_path
  end

  def destroy
    @todolist.destroy
    redirect_to todolists_path
  end

  private
    def set_todolist
      @todolist = Todolist.find(params[:id])
    end

    def todolist_params
      params.require(:todolist).permit(:name)
    end
end
