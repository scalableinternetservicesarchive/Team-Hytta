class PhotoalbumsController < ApplicationController
  before_action :set_photoalbum, only: [:show, :edit, :update, :destroy]

  def index
    @photoalbums = Photoalbum.all
  end

  def show
  end

  def new
    @photoalbum = Photoalbum.new
  end

  def edit
  end

  def create
    @photoalbum = Photoalbum.new(photoalbum_params)
    @photoalbum.save
    redirect_to photoalbums_path
  end

  def update
    @photoalbum.update(photoalbum_params)
    redirect_to photoalbums_path
  end

  def destroy
    @photoalbum.destroy
    redirect_to photoalbums_path
  end

  private
    def set_photoalbum
      @photoalbum = Photoalbum.find(params[:id])
    end

    def photoalbum_params
      params.require(:photoalbum).permit(:name, :description, :picture)
    end
end
