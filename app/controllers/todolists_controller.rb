class TodolistsController < ApplicationController
  before_action :set_todolist, only: [:show, :edit, :update, :destroy]
  before_action :set_cabin, only: [:index]
  respond_to :html, :json

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
    @todolist.user = current_user
    @todolist.save
    respond_with @todolist
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

    def set_cabin
      @cabin = Cabin.find(params[:cabin_id])
    end

    def todolist_params
      params.require(:todolist).permit(:name, :cabin_id)
    end
end
