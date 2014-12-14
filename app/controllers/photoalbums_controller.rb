class PhotoalbumsController < ApplicationController
  before_action :set_photoalbum, only: [:show, :edit, :update, :destroy]
  before_action :set_cabin, only: [:index]
  respond_to :html, :json

  def index
    #@photoalbums = Photoalbum.all
    @photoalbums = Photoalbum.paginate(:page => params[:page], :per_page => 30)
    respond_with @photoalbums, @cabin
  end

  def show
  end

  def new
   #@cabin = Cabin.find(params[:cabin_id])
    @photoalbum = Photoalbum.new
  end

  def edit
  end

  def create
    #@cabin = Cabin.find(params[:cabin_id])
    @photoalbum = Photoalbum.new(photoalbum_params)
    @photoalbum.user = current_user
    @photoalbum.save
    respond_with @photoalbum
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

    def set_cabin
      @cabin = Cabin.find(params[:cabin_id])
    end

    def photoalbum_params
      params.require(:photoalbum).permit(:name, :description, :picture, :cabin_id)
    end
end
